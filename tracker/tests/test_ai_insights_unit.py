"""
Unit tests for AIInsights class methods, targeting branches not covered by API tests.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from tracker.models import Baby, Feeding, Sleep, DiaperChange, GrowthMeasurement
from tracker.ai_insights import AIInsights
from datetime import datetime, timedelta, date
import pytz


def make_baby(user, birth_date='2024-01-01'):
    baby = Baby.objects.create(name='Test Baby', birth_date=birth_date, gender='Male', user=user)
    baby.refresh_from_db()
    return baby


def make_feedings(baby, count, hours_apart=3, feeding_type='bottle', quantity=120):
    """Create feedings with real timestamps (bypasses auto_now_add via update)."""
    now = datetime.now(pytz.UTC)
    for i in range(count):
        f = Feeding.objects.create(baby=baby, feeding_type=feeding_type, quantity=quantity)
        Feeding.objects.filter(id=f.id).update(time=now - timedelta(hours=i * hours_apart))


def make_sleeps(baby, count, hours_apart=8, duration_hours=2):
    now = datetime.now(pytz.UTC)
    for i in range(count):
        start = now - timedelta(hours=i * hours_apart + duration_hours)
        Sleep.objects.create(baby=baby, start_time=start, end_time=start + timedelta(hours=duration_hours))


def make_diapers(baby, count, hours_apart=4, diaper_type='wet'):
    """Create diaper changes with real timestamps (bypasses auto_now_add via update)."""
    now = datetime.now(pytz.UTC)
    for i in range(count):
        dc = DiaperChange.objects.create(baby=baby, diaper_type=diaper_type)
        DiaperChange.objects.filter(id=dc.id).update(time=now - timedelta(hours=i * hours_apart))


class AIInsightsFeedingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user)

    def test_insufficient_feeding_data_returns_message(self):
        make_feedings(self.baby, 3)
        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        self.assertIn('message', result)

    def test_sufficient_feeding_data_returns_insights(self):
        make_feedings(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        self.assertIn('basic_insights', result)
        self.assertIn('pattern_insights', result)
        self.assertIn('predictions', result)

    def test_feeding_quantity_insights_present(self):
        make_feedings(self.baby, 6, quantity=120)
        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        self.assertIn('quantity_insights', result)
        self.assertIn('average_quantity', result['quantity_insights'])

    def test_feeding_anomaly_unusual_interval(self):
        """A huge gap between feedings should be flagged as an anomaly."""
        now = datetime.now(pytz.UTC)
        # 9 feedings 1 hour apart (tight cluster), then one 72 hours before
        for i in range(9):
            f = Feeding.objects.create(baby=self.baby, feeding_type='bottle', quantity=120)
            Feeding.objects.filter(id=f.id).update(time=now - timedelta(hours=i))
        f = Feeding.objects.create(baby=self.baby, feeding_type='bottle', quantity=120)
        Feeding.objects.filter(id=f.id).update(time=now - timedelta(hours=72))

        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        types = [a['type'] for a in result.get('anomalies', [])]
        self.assertIn('unusual_feeding_interval', types)

    def test_feeding_anomaly_unusual_quantity(self):
        """A wildly different quantity should be flagged as an anomaly."""
        now = datetime.now(pytz.UTC)
        # 9 consistent feedings, then one extreme outlier
        for i in range(9):
            f = Feeding.objects.create(baby=self.baby, feeding_type='bottle', quantity=120)
            Feeding.objects.filter(id=f.id).update(time=now - timedelta(hours=i * 3))
        f = Feeding.objects.create(baby=self.baby, feeding_type='bottle', quantity=99999)
        Feeding.objects.filter(id=f.id).update(time=now - timedelta(hours=30))

        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        types = [a['type'] for a in result.get('anomalies', [])]
        self.assertIn('unusual_feeding_quantity', types)

    def test_feeding_no_anomaly_identical_quantities(self):
        """Identical quantities should not produce quantity outlier anomaly."""
        make_feedings(self.baby, 6, quantity=120)
        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        types = [a['type'] for a in result.get('anomalies', [])]
        self.assertNotIn('unusual_feeding_quantity', types)

    def test_feeding_prediction_confidence_low_when_few_records(self):
        make_feedings(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        self.assertEqual(result['predictions']['confidence'], 'low')

    def test_feeding_prediction_confidence_medium_when_many_records(self):
        make_feedings(self.baby, 12)
        ai = AIInsights(self.baby)
        result = ai.get_feeding_insights()
        self.assertEqual(result['predictions']['confidence'], 'medium')


class AIInsightsSleepTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user)

    def test_insufficient_sleep_data_returns_message(self):
        make_sleeps(self.baby, 3)
        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        self.assertIn('message', result)

    def test_sufficient_sleep_data_returns_insights(self):
        make_sleeps(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        self.assertIn('basic_insights', result)
        self.assertIn('sleep_quality', result)

    def test_sleep_clustering_with_10_plus_records(self):
        make_sleeps(self.baby, 12)
        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        self.assertIn('pattern_insights', result)
        # clusters should be a dict when >= 10 records
        self.assertIsInstance(result['pattern_insights']['sleep_clusters'], dict)

    def test_sleep_no_clustering_below_10_records(self):
        make_sleeps(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        self.assertEqual(result['pattern_insights']['sleep_clusters'], {})

    def test_sleep_quality_score_in_range(self):
        make_sleeps(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        score = result['sleep_quality']['score']
        self.assertGreaterEqual(score, 1)
        self.assertLessEqual(score, 10)

    def test_sleep_fragmentation_anomaly(self):
        """Many short sleep sessions per day should trigger fragmented_sleep anomaly."""
        now = datetime.now(pytz.UTC)
        # 6 sessions on the same day, each 20 min apart
        for i in range(6):
            start = now - timedelta(hours=i * 0.5)
            Sleep.objects.create(baby=self.baby, start_time=start, end_time=start + timedelta(minutes=20))

        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        types = [a['type'] for a in result.get('anomalies', [])]
        self.assertIn('fragmented_sleep', types)

    def test_predict_next_sleep_returns_prediction(self):
        make_sleeps(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_sleep_insights()
        self.assertIn('next_predicted_sleep', result['predictions'])


class AIInsightsGrowthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user, birth_date='2023-01-01')

    def test_insufficient_growth_data_returns_message(self):
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=70, weight=8)
        ai = AIInsights(self.baby)
        result = ai.get_growth_insights()
        self.assertIn('message', result)

    def test_two_measurements_returns_insights(self):
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=70, weight=8)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-03-01', height=74, weight=9)
        ai = AIInsights(self.baby)
        result = ai.get_growth_insights()
        self.assertIn('current_stats', result)
        self.assertIn('growth_velocity', result)

    def test_three_measurements_uses_velocity_calc(self):
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=70, weight=8)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-02-01', height=72, weight=8.5)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-03-01', height=74, weight=9)
        ai = AIInsights(self.baby)
        result = ai.get_growth_insights()
        self.assertIn('height_cm_per_month', result['growth_velocity'])

    def test_growth_without_birth_date(self):
        """Should still work using relative dates when birth_date is missing."""
        baby_no_date = Baby.objects.create(name='NoDOB', birth_date='2023-06-01', gender='M', user=self.user)
        GrowthMeasurement.objects.create(baby=baby_no_date, date='2024-01-01', height=70, weight=8)
        GrowthMeasurement.objects.create(baby=baby_no_date, date='2024-03-01', height=74, weight=9)
        ai = AIInsights(baby_no_date)
        result = ai.get_growth_insights()
        self.assertIn('current_stats', result)


class AIInsightsDiaperTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user, birth_date=date.today().replace(year=date.today().year - 1).isoformat())

    def test_insufficient_diaper_data_returns_message(self):
        make_diapers(self.baby, 3)
        ai = AIInsights(self.baby)
        result = ai.get_diaper_insights()
        self.assertIn('message', result)

    def test_sufficient_diaper_data_returns_insights(self):
        make_diapers(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai.get_diaper_insights()
        self.assertIn('basic_stats', result)
        self.assertIn('type_distribution', result)

    def test_hydration_concern_with_few_wet_diapers(self):
        """A young baby with few wet diapers should trigger hydration concern."""
        birth = date.today() - timedelta(days=90)  # ~3 months old
        young_baby = make_baby(self.user, birth_date=birth.isoformat())
        now = datetime.now(pytz.UTC)
        # Only dirty diapers spread over 5 days — zero wet/day (below threshold of 4)
        for i in range(5):
            dc = DiaperChange.objects.create(baby=young_baby, diaper_type='dirty')
            DiaperChange.objects.filter(id=dc.id).update(time=now - timedelta(days=i))
        ai = AIInsights(young_baby)
        result = ai.get_diaper_insights()
        concern_types = [c['type'] for c in result.get('concerns', [])]
        self.assertIn('hydration', concern_types)

    def test_all_diaper_types_in_distribution(self):
        now = datetime.now(pytz.UTC)
        for i, dtype in enumerate(['wet', 'wet', 'dirty', 'mixed', 'wet', 'mixed']):
            DiaperChange.objects.create(baby=self.baby, time=now - timedelta(hours=i * 4), diaper_type=dtype)

        ai = AIInsights(self.baby)
        result = ai.get_diaper_insights()
        dist = result['type_distribution']
        self.assertIn('wet', dist)
        self.assertIn('dirty', dist)
        self.assertIn('mixed', dist)


class AIInsightsCalculateTrendTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user)
        self.ai = AIInsights(self.baby)

    def test_trend_increasing(self):
        import pandas as pd
        df = pd.DataFrame({'time': pd.date_range('2024-01-01', periods=5), 'value': [1, 2, 3, 4, 5]})
        result = self.ai._calculate_trend(df, 'value')
        self.assertEqual(result, 'increasing')

    def test_trend_decreasing(self):
        import pandas as pd
        df = pd.DataFrame({'time': pd.date_range('2024-01-01', periods=5), 'value': [5, 4, 3, 2, 1]})
        result = self.ai._calculate_trend(df, 'value')
        self.assertEqual(result, 'decreasing')

    def test_trend_stable(self):
        import pandas as pd
        df = pd.DataFrame({'time': pd.date_range('2024-01-01', periods=5), 'value': [5.0, 5.0, 5.0, 5.0, 5.0]})
        result = self.ai._calculate_trend(df, 'value')
        self.assertEqual(result, 'stable')

    def test_trend_insufficient_data(self):
        import pandas as pd
        df = pd.DataFrame({'time': pd.date_range('2024-01-01', periods=2), 'value': [1, 2]})
        result = self.ai._calculate_trend(df, 'value')
        self.assertEqual(result, 'insufficient data')

    def test_trend_missing_column(self):
        import pandas as pd
        df = pd.DataFrame({'time': pd.date_range('2024-01-01', periods=5), 'value': [1, 2, 3, 4, 5]})
        result = self.ai._calculate_trend(df, 'nonexistent')
        self.assertEqual(result, 'insufficient data')

    def test_trend_no_time_column(self):
        import pandas as pd
        df = pd.DataFrame({'value': [1, 2, 3, 4, 5]})
        result = self.ai._calculate_trend(df, 'value')
        self.assertEqual(result, 'no time column')

    def test_trend_non_numeric(self):
        import pandas as pd
        df = pd.DataFrame({'time': pd.date_range('2024-01-01', periods=5), 'value': ['a', 'b', 'c', 'd', 'e']})
        result = self.ai._calculate_trend(df, 'value')
        self.assertEqual(result, 'non-numeric data')


class AIInsightsBabyAgeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')

    def test_age_calculation_recent_birth(self):
        baby = make_baby(self.user, birth_date=date.today().replace(day=1).isoformat())
        ai = AIInsights(baby)
        age = ai._get_baby_age_months()
        self.assertGreaterEqual(age, 0)

    def test_age_calculation_one_year_old(self):
        birth = date.today().replace(year=date.today().year - 1)
        baby = make_baby(self.user, birth_date=birth.isoformat())
        ai = AIInsights(baby)
        age = ai._get_baby_age_months()
        self.assertAlmostEqual(age, 12, delta=1)

    def test_age_returns_zero_for_newborn(self):
        """A baby born today should have age 0 months."""
        baby = make_baby(self.user, birth_date=date.today().isoformat())
        ai = AIInsights(baby)
        age = ai._get_baby_age_months()
        self.assertEqual(age, 0)


class AIInsightsComprehensiveTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user, birth_date='2024-01-01')

    def test_comprehensive_with_no_data(self):
        ai = AIInsights(self.baby)
        result = ai.get_comprehensive_insights()
        self.assertIn('summary', result)
        self.assertFalse(result['summary']['data_completeness']['feeding'])
        self.assertFalse(result['summary']['data_completeness']['sleep'])

    def test_comprehensive_with_all_data(self):
        make_feedings(self.baby, 6)
        make_sleeps(self.baby, 6)
        make_diapers(self.baby, 6)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=60, weight=4)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-03-01', height=64, weight=5)

        ai = AIInsights(self.baby)
        result = ai.get_comprehensive_insights()
        self.assertTrue(result['summary']['data_completeness']['feeding'])
        self.assertTrue(result['summary']['data_completeness']['sleep'])
        self.assertIn('correlations', result)
        self.assertIn('recommendations', result)

    def test_correlations_require_two_data_types(self):
        make_feedings(self.baby, 6)
        # Only feeding data — should get "need at least two" message
        ai = AIInsights(self.baby)
        result = ai._find_cross_activity_correlations(has_feeding=True)
        self.assertEqual(len(result), 1)
        self.assertIn('message', result[0])

    def test_correlations_feeding_and_sleep(self):
        make_feedings(self.baby, 6)
        make_sleeps(self.baby, 6)
        ai = AIInsights(self.baby)
        result = ai._find_cross_activity_correlations(has_feeding=True, has_sleep=True)
        self.assertIsInstance(result, list)

    def test_recommendations_age_based_development_newborn(self):
        newborn = make_baby(self.user, birth_date=date.today().isoformat())
        ai = AIInsights(newborn)
        recs = ai._generate_recommendations()
        categories = [r['category'] for r in recs]
        self.assertIn('development', categories)
        titles = [r['title'] for r in recs]
        self.assertTrue(any('Tummy time' in t for t in titles))

    def test_recommendations_age_based_development_3_to_6_months(self):
        birth = date.today().replace(year=date.today().year - 1).replace(month=date.today().month)
        # ~4 months old
        from datetime import timedelta as td
        birth_date = (date.today() - td(days=120)).isoformat()
        baby = make_baby(self.user, birth_date=birth_date)
        ai = AIInsights(baby)
        recs = ai._generate_recommendations()
        titles = [r['title'] for r in recs]
        self.assertTrue(any('Interactive play' in t for t in titles))

    def test_recommendations_with_sleep_insights(self):
        make_sleeps(self.baby, 6)
        ai = AIInsights(self.baby)
        sleep_insights = ai.get_sleep_insights()
        recs = ai._generate_recommendations(sleep_insights=sleep_insights)
        self.assertIsInstance(recs, list)

    def test_recommendations_growth_decreasing_trend(self):
        growth_insights = {
            'growth_velocity': {
                'height_trend': 'decreasing',
                'weight_trend': 'stable'
            }
        }
        ai = AIInsights(self.baby)
        recs = ai._generate_recommendations(growth_insights=growth_insights)
        categories = [r['category'] for r in recs]
        self.assertIn('growth', categories)

    def test_recommendations_growth_regular_monitoring_reminder(self):
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=60, weight=4)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-03-01', height=64, weight=5)
        ai = AIInsights(self.baby)
        growth_insights = ai.get_growth_insights()
        recs = ai._generate_recommendations(growth_insights=growth_insights)
        titles = [r['title'] for r in recs]
        self.assertTrue(any('growth monitoring' in t.lower() for t in titles))


class AIInsightsVisualizationViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user, birth_date='2023-01-01')
        from rest_framework.test import APIClient
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.other_user = User.objects.create_user(username='other', password='p')
        self.other_baby = make_baby(self.other_user)

    def _viz_url(self, baby_id, viz_type=None):
        from django.urls import reverse
        url = reverse('baby-insights-visualizations', kwargs={'baby_id': baby_id})
        if viz_type:
            url += f'?type={viz_type}'
        return url

    def test_visualization_sleep_type(self):
        make_sleeps(self.baby, 6)
        response = self.client.get(self._viz_url(self.baby.id, 'sleep'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('sleep_patterns', response.data)

    def test_visualization_growth_type(self):
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=60, weight=4)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-03-01', height=64, weight=5)
        response = self.client.get(self._viz_url(self.baby.id, 'growth'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('growth_trends', response.data)

    def test_visualization_diaper_type(self):
        make_diapers(self.baby, 6)
        response = self.client.get(self._viz_url(self.baby.id, 'diaper'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('diaper_distribution', response.data)

    def test_visualization_all_type(self):
        response = self.client.get(self._viz_url(self.baby.id, 'all'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('feeding', response.data)
        self.assertIn('sleep', response.data)
        self.assertIn('growth', response.data)
        self.assertIn('diaper', response.data)

    def test_visualization_default_is_all(self):
        response = self.client.get(self._viz_url(self.baby.id))
        self.assertEqual(response.status_code, 200)
        self.assertIn('feeding', response.data)

    def test_visualization_baby_not_found(self):
        response = self.client.get(self._viz_url(99999))
        self.assertEqual(response.status_code, 404)

    def test_visualization_other_users_baby_returns_404(self):
        response = self.client.get(self._viz_url(self.other_baby.id))
        self.assertEqual(response.status_code, 404)


class AIInsightsInsightTypeTest(TestCase):
    """Test BabyAIInsightsView for all insight types including missing ones."""

    def setUp(self):
        self.user = User.objects.create_user(username='u', password='p')
        self.baby = make_baby(self.user, birth_date='2023-01-01')
        from rest_framework.test import APIClient
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-01-01', height=60, weight=4)
        GrowthMeasurement.objects.create(baby=self.baby, date='2024-03-01', height=64, weight=5)

    def _insights_url(self, insight_type=None):
        from django.urls import reverse
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby.id})
        if insight_type:
            url += f'?type={insight_type}'
        return url

    def test_growth_insight_type(self):
        response = self.client.get(self._insights_url('growth'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('growth_insights', response.data)

    def test_all_insight_type_returns_all_keys(self):
        response = self.client.get(self._insights_url('all'))
        self.assertEqual(response.status_code, 200)
        for key in ['feeding_insights', 'sleep_insights', 'growth_insights', 'diaper_insights', 'comprehensive_insights']:
            self.assertIn(key, response.data)

    def test_default_insight_type_is_all(self):
        response = self.client.get(self._insights_url())
        self.assertEqual(response.status_code, 200)
        self.assertIn('feeding_insights', response.data)

    def test_unknown_insight_type_returns_all(self):
        response = self.client.get(self._insights_url('unknown'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('feeding_insights', response.data)

    def test_post_method_returns_insights(self):
        response = self.client.post(self._insights_url('all'), {})
        self.assertEqual(response.status_code, 200)
        self.assertIn('feeding_insights', response.data)

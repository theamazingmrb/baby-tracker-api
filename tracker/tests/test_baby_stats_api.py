from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, Feeding, Sleep
from datetime import datetime, timedelta, date
import pytz


class BabyStatsAPITestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1', email='test1@example.com', password='testpassword1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2', email='test2@example.com', password='testpassword2'
        )

        self.baby1 = Baby.objects.create(
            name='Baby One', birth_date='2023-01-01', gender='Male', user=self.user1
        )
        self.baby2 = Baby.objects.create(
            name='Baby Two', birth_date='2023-02-01', gender='Female', user=self.user2
        )

        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)

        self.unauthenticated_client = APIClient()

    def _stats_url(self, baby_id):
        return reverse('baby-stats', kwargs={'baby_id': baby_id})

    def test_stats_with_no_data(self):
        """Stats with no feedings or sleep should return zeros."""
        response = self.client1.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feedings_today'], 0)
        self.assertEqual(response.data['total_sleep_hours'], 0)

    def test_stats_counts_feedings_today(self):
        now = datetime.now(pytz.UTC)
        for _ in range(2):
            f = Feeding.objects.create(baby=self.baby1, feeding_type='bottle', quantity=120)
            Feeding.objects.filter(id=f.id).update(time=now)

        response = self.client1.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feedings_today'], 2)

    def test_stats_does_not_count_old_feedings(self):
        now = datetime.now(pytz.UTC)
        f = Feeding.objects.create(baby=self.baby1, feeding_type='bottle', quantity=120)
        Feeding.objects.filter(id=f.id).update(time=now - timedelta(days=2))

        response = self.client1.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feedings_today'], 0)

    def test_stats_totals_sleep_last_7_days(self):
        now = datetime.now(pytz.UTC)
        Sleep.objects.create(
            baby=self.baby1,
            start_time=now - timedelta(hours=10),
            end_time=now - timedelta(hours=8)
        )
        Sleep.objects.create(
            baby=self.baby1,
            start_time=now - timedelta(hours=4),
            end_time=now - timedelta(hours=2)
        )

        response = self.client1.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertAlmostEqual(response.data['total_sleep_hours'], 4.0, places=1)

    def test_stats_excludes_sleep_older_than_7_days(self):
        now = datetime.now(pytz.UTC)
        Sleep.objects.create(
            baby=self.baby1,
            start_time=now - timedelta(days=10),
            end_time=now - timedelta(days=10) + timedelta(hours=8)
        )

        response = self.client1.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_sleep_hours'], 0)

    def test_stats_ignores_ongoing_sleep(self):
        """Sleep sessions with no end_time should not be counted."""
        now = datetime.now(pytz.UTC)
        Sleep.objects.create(baby=self.baby1, start_time=now - timedelta(hours=1), end_time=None)

        response = self.client1.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_sleep_hours'], 0)

    def test_stats_baby_not_found(self):
        response = self.client1.get(self._stats_url(99999))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_stats_cannot_access_other_users_baby(self):
        response = self.client1.get(self._stats_url(self.baby2.id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_stats_unauthenticated(self):
        response = self.unauthenticated_client.get(self._stats_url(self.baby1.id))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

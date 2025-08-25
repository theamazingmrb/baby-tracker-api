from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, Feeding, Sleep, DiaperChange
from datetime import datetime, timedelta
import pytz
import json


class AIInsightsAPITestCase(TestCase):
    def setUp(self):
        # Create test users
        self.user1 = User.objects.create_user(
            username='testuser1',
            email='test1@example.com',
            password='testpassword1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='testpassword2'
        )
        
        # Create babies for each user
        self.baby1 = Baby.objects.create(
            name='Baby One',
            birth_date='2023-01-01',
            gender='Male',
            user=self.user1
        )
        
        self.baby2 = Baby.objects.create(
            name='Baby Two',
            birth_date='2023-02-01',
            gender='Female',
            user=self.user2
        )
        
        # Get current time for creating records
        now = datetime.now(pytz.UTC)
        
        # Create some feeding records for baby1
        for i in range(5):
            time_offset = now - timedelta(hours=i*4)
            Feeding.objects.create(
                baby=self.baby1,
                time=time_offset,
                feeding_type='breastfeeding',
                quantity=60,
                last_side='left_feeding'
            )
        
        # Create some sleep records for baby1
        for i in range(3):
            time_offset = now - timedelta(hours=i*8)
            Sleep.objects.create(
                baby=self.baby1,
                start_time=time_offset - timedelta(hours=2),
                end_time=time_offset
            )
        
        # Create some diaper change records for baby1
        for i in range(6):
            time_offset = now - timedelta(hours=i*4)
            DiaperChange.objects.create(
                baby=self.baby1,
                time=time_offset,
                diaper_type='wet'
            )
        
        # Create some records for baby2 as well
        for i in range(3):
            time_offset = now - timedelta(hours=i*4)
            Feeding.objects.create(
                baby=self.baby2,
                time=time_offset,
                feeding_type='bottle',
                quantity=120,
                last_side=None
            )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_feeding_insights_endpoint(self):
        """Test feeding insights endpoint"""
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=feeding'
        
        # Test owner can get feeding insights for their baby
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify response contains expected fields
        self.assertIn('feeding_insights', response.data)
        
        # Test non-owner cannot get feeding insights for another user's baby
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=feeding'
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot get feeding insights
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_sleep_insights_endpoint(self):
        """Test sleep insights endpoint"""
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=sleep'
        
        # Test owner can get sleep insights for their baby
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify response contains expected fields
        self.assertIn('sleep_insights', response.data)
        
        # Test non-owner cannot get sleep insights for another user's baby
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=sleep'
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot get sleep insights
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_diaper_insights_endpoint(self):
        """Test diaper insights endpoint"""
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=diaper'
        
        # Test owner can get diaper insights for their baby
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify response contains expected fields
        self.assertIn('diaper_insights', response.data)
        
        # Test non-owner cannot get diaper insights for another user's baby
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=diaper'
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot get diaper insights
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_overall_insights_endpoint(self):
        """Test overall insights endpoint"""
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=comprehensive'
        
        # Test owner can get overall insights for their baby
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify response contains expected fields
        self.assertIn('comprehensive_insights', response.data)
        
        # Test non-owner cannot get overall insights for another user's baby
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=comprehensive'
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot get overall insights
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_generate_report_endpoint(self):
        """Test generate report endpoint"""
        url = reverse('baby-ai-insights', kwargs={'baby_id': self.baby1.id}) + '?type=all'
        
        # Test owner can generate a report for their baby
        data = {
            'start_date': (datetime.now(pytz.UTC) - timedelta(days=7)).date().isoformat(),
            'end_date': datetime.now(pytz.UTC).date().isoformat(),
            'report_type': 'summary'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify response contains expected fields
        self.assertIn('feeding_insights', response.data)
        self.assertIn('sleep_insights', response.data)
        self.assertIn('growth_insights', response.data)
        self.assertIn('diaper_insights', response.data)
        self.assertIn('comprehensive_insights', response.data)
        
        # Test non-owner cannot generate a report for another user's baby
        response = self.client2.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot generate a report
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_prediction_endpoint(self):
        """Test prediction endpoint"""
        url = reverse('baby-insights-visualizations', kwargs={'baby_id': self.baby1.id}) + '?type=feeding'
        
        # Test owner can get predictions for their baby
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify response contains expected fields
        self.assertIn('feeding_patterns', response.data)
        
        # Test non-owner cannot get predictions for another user's baby
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot get predictions
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

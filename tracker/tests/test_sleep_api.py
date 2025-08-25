from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, Sleep
from datetime import datetime, timedelta
import pytz


class SleepAPITestCase(TestCase):
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
        
        # Get current time for sleep records
        now = datetime.now(pytz.UTC)
        one_hour_ago = now - timedelta(hours=1)
        two_hours_ago = now - timedelta(hours=2)
        
        # Create sleep records for each baby
        self.sleep1 = Sleep.objects.create(
            baby=self.baby1,
            start_time=two_hours_ago,
            end_time=one_hour_ago
        )
        
        self.sleep2 = Sleep.objects.create(
            baby=self.baby2,
            start_time=one_hour_ago,
            end_time=None  # Ongoing sleep
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_sleep_list_endpoint(self):
        """Test sleep list endpoint"""
        url = reverse('sleep-list')
        
        # Test authenticated user can list their sleep records
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        
        # Test second user can list their sleep records
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertIsNone(response.data[0]['end_time'])  # Verify ongoing sleep
        
        # Test unauthenticated user cannot list sleep records
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_sleep_create_endpoint(self):
        """Test sleep create endpoint"""
        url = reverse('sleep-list')
        
        # Get current time for new sleep record
        now = datetime.now(pytz.UTC)
        three_hours_ago = now - timedelta(hours=3)
        
        # Test authenticated user can create a sleep record for their baby
        data = {
            'baby': self.baby1.id,
            'start_time': three_hours_ago.isoformat(),
            'end_time': now.isoformat()
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        
        # Verify sleep record was created in database
        self.assertEqual(Sleep.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create sleep record for another user's baby
        data = {
            'baby': self.baby2.id,
            'start_time': three_hours_ago.isoformat(),
            'end_time': now.isoformat()
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a sleep record
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_sleep_retrieve_endpoint(self):
        """Test sleep retrieve endpoint"""
        url = reverse('sleep-detail', kwargs={'pk': self.sleep1.id})
        
        # Test owner can retrieve their sleep record
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['baby'], self.baby1.id)
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_sleep_update_endpoint(self):
        """Test sleep update endpoint"""
        url = reverse('sleep-detail', kwargs={'pk': self.sleep1.id})
        
        # Get current time for updated sleep record
        now = datetime.now(pytz.UTC)
        
        # Test owner can update their sleep record
        data = {
            'baby': self.baby1.id,
            'start_time': self.sleep1.start_time.isoformat(),
            'end_time': now.isoformat()
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify sleep record was updated in database
        self.sleep1.refresh_from_db()
        self.assertEqual(self.sleep1.end_time.replace(microsecond=0), now.replace(microsecond=0))
        
        # Test non-owner cannot update
        url = reverse('sleep-detail', kwargs={'pk': self.sleep2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_sleep_delete_endpoint(self):
        """Test sleep delete endpoint"""
        url = reverse('sleep-detail', kwargs={'pk': self.sleep1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Sleep.objects.filter(id=self.sleep1.id).count(), 1)
        
        # Test owner can delete their sleep record
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify sleep record was deleted from database
        self.assertEqual(Sleep.objects.filter(id=self.sleep1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('sleep-detail', kwargs={'pk': self.sleep2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Sleep.objects.filter(id=self.sleep2.id).count(), 1)

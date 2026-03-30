from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, GrowthMeasurement
from datetime import datetime, date
import pytz


class GrowthMilestoneAPITestCase(TestCase):
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
        
        # Create growth measurements for each baby
        self.growth_measurement1 = GrowthMeasurement.objects.create(
            baby=self.baby1,
            date='2023-03-01',
            height=60.5,
            weight=5.2,
            notes='3-month checkup'
        )
        
        self.growth_measurement2 = GrowthMeasurement.objects.create(
            baby=self.baby2,
            date='2023-04-01',
            height=62.0,
            weight=6.1,
            notes='4-month checkup'
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_growth_measurement_list_endpoint(self):
        """Test growth measurement list endpoint"""
        url = reverse('growth-measurement-list')
        
        # Test authenticated user can list their growth measurements
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        self.assertEqual(float(response.data[0]['height']), 60.5)
        self.assertEqual(float(response.data[0]['weight']), 5.2)
        
        # Test second user can list their growth measurements
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertEqual(float(response.data[0]['height']), 62.0)
        self.assertEqual(float(response.data[0]['weight']), 6.1)
        
        # Test unauthenticated user cannot list growth measurements
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_measurement_create_endpoint(self):
        """Test growth measurement create endpoint"""
        url = reverse('growth-measurement-list')
        
        # Test authenticated user can create a growth measurement for their baby
        data = {
            'baby': self.baby1.id,
            'date': '2023-06-01',
            'height': 65.0,
            'weight': 6.5,
            'notes': '6-month checkup'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(float(response.data['height']), 65.0)
        self.assertEqual(float(response.data['weight']), 6.5)
        self.assertEqual(response.data['notes'], '6-month checkup')
        
        # Verify growth measurement was created in database
        self.assertEqual(GrowthMeasurement.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create growth measurement for another user's baby
        data = {
            'baby': self.baby2.id,
            'date': '2023-06-01',
            'height': 65.0,
            'weight': 6.5,
            'notes': 'Unauthorized measurement'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a growth measurement
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_measurement_retrieve_endpoint(self):
        """Test growth measurement retrieve endpoint"""
        url = reverse('growth-measurement-detail', kwargs={'pk': self.growth_measurement1.id})
        
        # Test owner can retrieve their growth measurement
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(float(response.data['height']), 60.5)
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_measurement_update_endpoint(self):
        """Test growth measurement update endpoint"""
        url = reverse('growth-measurement-detail', kwargs={'pk': self.growth_measurement1.id})
        
        # Test owner can update their growth measurement
        data = {
            'baby': self.baby1.id,
            'date': '2023-03-01',
            'height': 61.0,
            'weight': 5.3,
            'notes': 'Updated 3-month checkup'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.data['height']), 61.0)
        self.assertEqual(float(response.data['weight']), 5.3)
        self.assertEqual(response.data['notes'], 'Updated 3-month checkup')
        
        # Verify growth measurement was updated in database
        self.growth_measurement1.refresh_from_db()
        self.assertEqual(self.growth_measurement1.height, 61.0)
        self.assertEqual(self.growth_measurement1.weight, 5.3)
        
        # Test non-owner cannot update
        url = reverse('growth-measurement-detail', kwargs={'pk': self.growth_measurement2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_measurement_delete_endpoint(self):
        """Test growth measurement delete endpoint"""
        url = reverse('growth-measurement-detail', kwargs={'pk': self.growth_measurement1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(GrowthMeasurement.objects.filter(id=self.growth_measurement1.id).count(), 1)
        
        # Test owner can delete their growth measurement
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify growth measurement was deleted from database
        self.assertEqual(GrowthMeasurement.objects.filter(id=self.growth_measurement1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('growth-measurement-detail', kwargs={'pk': self.growth_measurement2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(GrowthMeasurement.objects.filter(id=self.growth_measurement2.id).count(), 1)

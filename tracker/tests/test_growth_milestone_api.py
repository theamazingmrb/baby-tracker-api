from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, GrowthMilestone
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
        
        # Create growth milestones for each baby
        self.growth_milestone1 = GrowthMilestone.objects.create(
            baby=self.baby1,
            date='2023-03-01',
            height=60.5,
            weight=5.2,
            notes='3-month checkup'
        )
        
        self.growth_milestone2 = GrowthMilestone.objects.create(
            baby=self.baby2,
            date='2023-04-01',
            height=62.0,
            weight=5.5,
            notes='2-month checkup'
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_growth_milestone_list_endpoint(self):
        """Test growth milestone list endpoint"""
        url = reverse('growth-milestone-list')
        
        # Test authenticated user can list their growth milestones
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        self.assertEqual(float(response.data[0]['height']), 60.5)
        self.assertEqual(float(response.data[0]['weight']), 5.2)
        
        # Test second user can list their growth milestones
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertEqual(float(response.data[0]['height']), 62.0)
        self.assertEqual(float(response.data[0]['weight']), 5.5)
        
        # Test unauthenticated user cannot list growth milestones
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_milestone_create_endpoint(self):
        """Test growth milestone create endpoint"""
        url = reverse('growth-milestone-list')
        
        # Test authenticated user can create a growth milestone for their baby
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
        
        # Verify growth milestone was created in database
        self.assertEqual(GrowthMilestone.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create growth milestone for another user's baby
        data = {
            'baby': self.baby2.id,
            'date': '2023-06-01',
            'height': 65.0,
            'weight': 6.5,
            'notes': 'Unauthorized milestone'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a growth milestone
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_milestone_retrieve_endpoint(self):
        """Test growth milestone retrieve endpoint"""
        url = reverse('growth-milestone-detail', kwargs={'pk': self.growth_milestone1.id})
        
        # Test owner can retrieve their growth milestone
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
    
    def test_growth_milestone_update_endpoint(self):
        """Test growth milestone update endpoint"""
        url = reverse('growth-milestone-detail', kwargs={'pk': self.growth_milestone1.id})
        
        # Test owner can update their growth milestone
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
        
        # Verify growth milestone was updated in database
        self.growth_milestone1.refresh_from_db()
        self.assertEqual(self.growth_milestone1.height, 61.0)
        self.assertEqual(self.growth_milestone1.weight, 5.3)
        
        # Test non-owner cannot update
        url = reverse('growth-milestone-detail', kwargs={'pk': self.growth_milestone2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_growth_milestone_delete_endpoint(self):
        """Test growth milestone delete endpoint"""
        url = reverse('growth-milestone-detail', kwargs={'pk': self.growth_milestone1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(GrowthMilestone.objects.filter(id=self.growth_milestone1.id).count(), 1)
        
        # Test owner can delete their growth milestone
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify growth milestone was deleted from database
        self.assertEqual(GrowthMilestone.objects.filter(id=self.growth_milestone1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('growth-milestone-detail', kwargs={'pk': self.growth_milestone2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(GrowthMilestone.objects.filter(id=self.growth_milestone2.id).count(), 1)

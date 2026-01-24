from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, DiaperChange
from datetime import datetime
import pytz


class DiaperChangeAPITestCase(TestCase):
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
        
        # Create diaper changes for each baby
        self.diaper_change1 = DiaperChange.objects.create(
            baby=self.baby1,
            diaper_type='wet'
        )
        
        self.diaper_change2 = DiaperChange.objects.create(
            baby=self.baby2,
            diaper_type='dirty'
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_diaper_change_list_endpoint(self):
        """Test diaper change list endpoint"""
        url = reverse('diaper-change-list')
        
        # Test authenticated user can list their diaper changes
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        self.assertEqual(response.data[0]['diaper_type'], 'wet')
        
        # Test second user can list their diaper changes
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertEqual(response.data[0]['diaper_type'], 'dirty')
        
        # Test unauthenticated user cannot list diaper changes
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_diaper_change_create_endpoint(self):
        """Test diaper change create endpoint"""
        url = reverse('diaper-change-list')
        
        # Test authenticated user can create a diaper change for their baby
        data = {
            'baby': self.baby1.id,
            'diaper_type': 'mixed'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['diaper_type'], 'mixed')
        
        # Verify diaper change was created in database
        self.assertEqual(DiaperChange.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create diaper change for another user's baby
        data = {
            'baby': self.baby2.id,
            'diaper_type': 'wet'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a diaper change
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_diaper_change_retrieve_endpoint(self):
        """Test diaper change retrieve endpoint"""
        url = reverse('diaper-change-detail', kwargs={'pk': self.diaper_change1.id})
        
        # Test owner can retrieve their diaper change
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['diaper_type'], 'wet')
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_diaper_change_update_endpoint(self):
        """Test diaper change update endpoint"""
        url = reverse('diaper-change-detail', kwargs={'pk': self.diaper_change1.id})
        
        # Test owner can update their diaper change
        data = {
            'baby': self.baby1.id,
            'diaper_type': 'dirty'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['diaper_type'], 'dirty')
        
        # Verify diaper change was updated in database
        self.diaper_change1.refresh_from_db()
        self.assertEqual(self.diaper_change1.diaper_type, 'dirty')
        
        # Test non-owner cannot update
        url = reverse('diaper-change-detail', kwargs={'pk': self.diaper_change2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_diaper_change_delete_endpoint(self):
        """Test diaper change delete endpoint"""
        url = reverse('diaper-change-detail', kwargs={'pk': self.diaper_change1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(DiaperChange.objects.filter(id=self.diaper_change1.id).count(), 1)
        
        # Test owner can delete their diaper change
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify diaper change was deleted from database
        self.assertEqual(DiaperChange.objects.filter(id=self.diaper_change1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('diaper-change-detail', kwargs={'pk': self.diaper_change2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(DiaperChange.objects.filter(id=self.diaper_change2.id).count(), 1)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, Feeding
from datetime import datetime
import pytz


class FeedingAPITestCase(TestCase):
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
        
        # Create feedings for each baby
        self.feeding1 = Feeding.objects.create(
            baby=self.baby1,
            feeding_type='breastfeeding',
            quantity=4.0,
            last_side='left_feeding'
        )
        
        self.feeding2 = Feeding.objects.create(
            baby=self.baby2,
            feeding_type='bottle',
            quantity=3.0
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_feeding_list_endpoint(self):
        """Test feeding list endpoint"""
        url = reverse('feeding-list')
        
        # Test authenticated user can list their feedings
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        self.assertEqual(response.data[0]['feeding_type'], 'breastfeeding')
        
        # Test second user can list their feedings
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertEqual(response.data[0]['feeding_type'], 'bottle')
        
        # Test unauthenticated user cannot list feedings
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_feeding_create_endpoint(self):
        """Test feeding create endpoint"""
        url = reverse('feeding-list')
        
        # Test authenticated user can create a feeding for their baby
        data = {
            'baby': self.baby1.id,
            'feeding_type': 'solid',
            'quantity': 2.5,
            'last_side': 'right_feeding'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['feeding_type'], 'solid')
        self.assertEqual(float(response.data['quantity']), 2.5)
        
        # Verify feeding was created in database
        self.assertEqual(Feeding.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create feeding for another user's baby
        data = {
            'baby': self.baby2.id,
            'feeding_type': 'bottle',
            'quantity': 3.0
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a feeding
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_feeding_retrieve_endpoint(self):
        """Test feeding retrieve endpoint"""
        url = reverse('feeding-detail', kwargs={'pk': self.feeding1.id})
        
        # Test owner can retrieve their feeding
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['feeding_type'], 'breastfeeding')
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_feeding_update_endpoint(self):
        """Test feeding update endpoint"""
        url = reverse('feeding-detail', kwargs={'pk': self.feeding1.id})
        
        # Test owner can update their feeding
        data = {
            'baby': self.baby1.id,
            'feeding_type': 'bottle',
            'quantity': 5.0,
            'last_side': 'both_feeding'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['feeding_type'], 'bottle')
        self.assertEqual(float(response.data['quantity']), 5.0)
        self.assertEqual(response.data['last_side'], 'both_feeding')
        
        # Verify feeding was updated in database
        self.feeding1.refresh_from_db()
        self.assertEqual(self.feeding1.feeding_type, 'bottle')
        self.assertEqual(self.feeding1.quantity, 5.0)
        
        # Test non-owner cannot update
        url = reverse('feeding-detail', kwargs={'pk': self.feeding2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_feeding_delete_endpoint(self):
        """Test feeding delete endpoint"""
        url = reverse('feeding-detail', kwargs={'pk': self.feeding1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Feeding.objects.filter(id=self.feeding1.id).count(), 1)
        
        # Test owner can delete their feeding
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify feeding was deleted from database
        self.assertEqual(Feeding.objects.filter(id=self.feeding1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('feeding-detail', kwargs={'pk': self.feeding2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Feeding.objects.filter(id=self.feeding2.id).count(), 1)

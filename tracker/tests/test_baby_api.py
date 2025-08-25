from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby
from datetime import datetime, date
import pytz


class BabyAPITestCase(TestCase):
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
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_baby_list_endpoint(self):
        """Test baby list endpoint"""
        url = reverse('baby-list')
        
        # Test authenticated user can list their babies
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Baby One')
        
        # Test second user can list their babies
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Baby Two')
        
        # Test unauthenticated user cannot list babies
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_baby_create_endpoint(self):
        """Test baby create endpoint"""
        url = reverse('baby-list')
        
        # Test authenticated user can create a baby
        data = {
            'name': 'New Baby',
            'birth_date': '2023-03-01',
            'gender': 'Female'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Baby')
        self.assertEqual(response.data['gender'], 'Female')
        
        # Verify baby was created in database
        self.assertEqual(Baby.objects.filter(user=self.user1).count(), 2)
        
        # Test unauthenticated user cannot create a baby
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_baby_retrieve_endpoint(self):
        """Test baby retrieve endpoint"""
        url = reverse('baby-detail', kwargs={'pk': self.baby1.id})
        
        # Test owner can retrieve their baby
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Baby One')
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_baby_update_endpoint(self):
        """Test baby update endpoint"""
        url = reverse('baby-detail', kwargs={'pk': self.baby1.id})
        
        # Test owner can update their baby
        data = {
            'name': 'Updated Baby Name',
            'birth_date': '2023-01-01',
            'gender': 'Male'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Updated Baby Name')
        
        # Verify baby was updated in database
        self.baby1.refresh_from_db()
        self.assertEqual(self.baby1.name, 'Updated Baby Name')
        
        # Test non-owner cannot update
        response = self.client2.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_baby_delete_endpoint(self):
        """Test baby delete endpoint"""
        url = reverse('baby-detail', kwargs={'pk': self.baby1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Baby.objects.filter(id=self.baby1.id).count(), 1)
        
        # Test owner can delete their baby
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify baby was deleted from database
        self.assertEqual(Baby.objects.filter(id=self.baby1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('baby-detail', kwargs={'pk': self.baby2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Baby.objects.filter(id=self.baby2.id).count(), 1)

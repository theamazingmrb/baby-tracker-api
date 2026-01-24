from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, Milestone
from datetime import datetime, date
import pytz


class MilestoneAPITestCase(TestCase):
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
        
        # Create milestones for each baby
        self.milestone1 = Milestone.objects.create(
            baby=self.baby1,
            title='First Smile',
            date_achieved='2023-02-15',
            notes='Baby smiled for the first time',
            category='social'
        )
        
        self.milestone2 = Milestone.objects.create(
            baby=self.baby2,
            title='First Roll Over',
            date_achieved='2023-04-01',
            notes='Baby rolled over from back to tummy',
            category='physical'
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_milestone_list_endpoint(self):
        """Test milestone list endpoint"""
        url = reverse('milestone-list', kwargs={'baby_id': self.baby1.id})
        
        # Test authenticated user can list their milestones
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        self.assertEqual(response.data[0]['title'], 'First Smile')
        self.assertEqual(response.data[0]['category'], 'social')
        
        # Test second user can list their milestones
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertEqual(response.data[0]['title'], 'First Roll Over')
        self.assertEqual(response.data[0]['category'], 'physical')
        
        # Test unauthenticated user cannot list milestones
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_milestone_create_endpoint(self):
        """Test milestone create endpoint"""
        url = reverse('milestone-list', kwargs={'baby_id': self.baby1.id})
        
        # Test authenticated user can create a milestone for their baby
        data = {
            'baby': self.baby1.id,
            'title': 'First Word',
            'date_achieved': '2023-06-15',
            'notes': 'Baby said "mama" for the first time',
            'category': 'language'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['title'], 'First Word')
        self.assertEqual(response.data['category'], 'language')
        
        # Verify milestone was created in database
        self.assertEqual(Milestone.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create milestone for another user's baby
        data = {
            'baby': self.baby2.id,
            'title': 'Unauthorized Milestone',
            'date_achieved': '2023-06-15',
            'notes': 'This should not be allowed',
            'category': 'language'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a milestone
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_milestone_retrieve_endpoint(self):
        """Test milestone retrieve endpoint"""
        url = reverse('milestone-detail', kwargs={'baby_id': self.baby1.id, 'pk': self.milestone1.id})
        
        # Test owner can retrieve their milestone
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['title'], 'First Smile')
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_milestone_update_endpoint(self):
        """Test milestone update endpoint"""
        url = reverse('milestone-detail', kwargs={'baby_id': self.baby1.id, 'pk': self.milestone1.id})
        
        # Test owner can update their milestone
        data = {
            'baby': self.baby1.id,
            'title': 'First Real Smile',
            'date_achieved': '2023-02-16',
            'notes': 'Updated: Baby smiled intentionally for the first time',
            'category': 'social'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'First Real Smile')
        self.assertEqual(response.data['notes'], 'Updated: Baby smiled intentionally for the first time')
        
        # Verify milestone was updated in database
        self.milestone1.refresh_from_db()
        self.assertEqual(self.milestone1.title, 'First Real Smile')
        self.assertEqual(self.milestone1.notes, 'Updated: Baby smiled intentionally for the first time')
        
        # Test non-owner cannot update
        url = reverse('milestone-detail', kwargs={'baby_id': self.baby2.id, 'pk': self.milestone2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_milestone_delete_endpoint(self):
        """Test milestone delete endpoint"""
        url = reverse('milestone-detail', kwargs={'baby_id': self.baby1.id, 'pk': self.milestone1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Milestone.objects.filter(id=self.milestone1.id).count(), 1)
        
        # Test owner can delete their milestone
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify milestone was deleted from database
        self.assertEqual(Milestone.objects.filter(id=self.milestone1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('milestone-detail', kwargs={'baby_id': self.baby2.id, 'pk': self.milestone2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Milestone.objects.filter(id=self.milestone2.id).count(), 1)

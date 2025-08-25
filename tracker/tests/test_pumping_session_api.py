from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, PumpingSession
from datetime import datetime, timedelta
import pytz


class PumpingSessionAPITestCase(TestCase):
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
        
        # Get current time for pumping session records
        now = datetime.now(pytz.UTC)
        one_hour_ago = now - timedelta(hours=1)
        two_hours_ago = now - timedelta(hours=2)
        
        # Create pumping sessions for each user
        self.pumping_session1 = PumpingSession.objects.create(
            user=self.user1,
            time=two_hours_ago,
            side='both_pump',
            quantity=120
        )
        
        self.pumping_session2 = PumpingSession.objects.create(
            user=self.user2,
            time=one_hour_ago,
            side='right_pump',
            quantity=150
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_pumping_session_list_endpoint(self):
        """Test pumping session list endpoint"""
        url = reverse('pumping-session-list')
        
        # Test authenticated user can list their pumping sessions
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user1.id)
        self.assertEqual(response.data[0]['quantity'], 120)
        self.assertEqual(response.data[0]['side'], 'both_pump')
        
        # Test second user can list their pumping sessions
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['user'], self.user2.id)
        self.assertEqual(response.data[0]['quantity'], 150)
        self.assertEqual(response.data[0]['side'], 'right_pump')
        
        # Test unauthenticated user cannot list pumping sessions
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_pumping_session_create_endpoint(self):
        """Test pumping session create endpoint"""
        url = reverse('pumping-session-list')
        
        # Get current time for new pumping session
        now = datetime.now(pytz.UTC)
        start_time = now - timedelta(minutes=30)
        
        # Test authenticated user can create a pumping session
        data = {
            'time': now.isoformat(),
            'side': 'both_pump',
            'quantity': 100
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], self.user1.id)
        self.assertEqual(response.data['quantity'], 100)
        self.assertEqual(response.data['side'], 'both_pump')
        
        # Verify pumping session was created in database
        self.assertEqual(PumpingSession.objects.filter(user=self.user1).count(), 2)
        
        # Test user cannot create a pumping session for another user
        data = {
            'time': now.isoformat(),
            'side': 'left_pump',
            'quantity': 100
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # The session should be created for the authenticated user (user1), not user2
        self.assertEqual(response.data['user'], self.user1.id)
        
        # Test unauthenticated user cannot create a pumping session
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_pumping_session_retrieve_endpoint(self):
        """Test pumping session retrieve endpoint"""
        url = reverse('pumping-session-detail', kwargs={'pk': self.pumping_session1.id})
        
        # Test owner can retrieve their pumping session
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], self.user1.id)
        self.assertEqual(response.data['quantity'], 120)
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_pumping_session_update_endpoint(self):
        """Test pumping session update endpoint"""
        url = reverse('pumping-session-detail', kwargs={'pk': self.pumping_session1.id})
        
        # Get current time for updated pumping session
        now = datetime.now(pytz.UTC)
        start_time = now - timedelta(hours=3)
        end_time = now - timedelta(hours=2, minutes=30)
        
        # Test owner can update their pumping session
        data = {
            'time': start_time.isoformat(),
            'side': 'left_pump',
            'quantity': 130
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantity'], 130)
        self.assertEqual(response.data['side'], 'left_pump')
        
        # Verify pumping session was updated in database
        self.pumping_session1.refresh_from_db()
        self.assertEqual(self.pumping_session1.quantity, 130)
        self.assertEqual(self.pumping_session1.side, 'left_pump')
        
        # Test non-owner cannot update
        url = reverse('pumping-session-detail', kwargs={'pk': self.pumping_session2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_pumping_session_delete_endpoint(self):
        """Test pumping session delete endpoint"""
        url = reverse('pumping-session-detail', kwargs={'pk': self.pumping_session1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(PumpingSession.objects.filter(id=self.pumping_session1.id).count(), 1)
        
        # Test owner can delete their pumping session
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify pumping session was deleted from database
        self.assertEqual(PumpingSession.objects.filter(id=self.pumping_session1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('pumping-session-detail', kwargs={'pk': self.pumping_session2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(PumpingSession.objects.filter(id=self.pumping_session2.id).count(), 1)

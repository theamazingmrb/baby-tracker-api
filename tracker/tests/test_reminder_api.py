from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, Reminder
from datetime import datetime, timedelta
import pytz


class ReminderAPITestCase(TestCase):
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
        
        # Get current time for reminder records
        now = datetime.now(pytz.UTC)
        tomorrow = now + timedelta(days=1)
        day_after_tomorrow = now + timedelta(days=2)
        
        # Create reminders for each user
        self.reminder1 = Reminder.objects.create(
            user=self.user1,
            baby=self.baby1,
            message="Doctor's appointment",
            time=tomorrow
        )
        
        self.reminder2 = Reminder.objects.create(
            user=self.user2,
            baby=self.baby2,
            message="Vaccination",
            time=day_after_tomorrow
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_reminder_list_endpoint(self):
        """Test reminder list endpoint"""
        url = reverse('reminder-list')
        
        # Test authenticated user can list their reminders
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['message'], "Doctor's appointment")
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        
        # Test second user can list their reminders
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['message'], "Vaccination")
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        
        # Test unauthenticated user cannot list reminders
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_reminder_create_endpoint(self):
        """Test reminder create endpoint"""
        url = reverse('reminder-list')
        
        # Get current time for new reminder
        now = datetime.now(pytz.UTC)
        next_week = now + timedelta(days=7)
        
        # Test authenticated user can create a reminder for their baby
        data = {
            'baby': self.baby1.id,
            'message': 'Growth check',
            'time': next_week.isoformat()
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['message'], 'Growth check')
        
        # Verify reminder was created in database
        self.assertEqual(Reminder.objects.filter(user=self.user1).count(), 2)
        
        # Test user cannot create reminder for another user's baby
        data = {
            'baby': self.baby2.id,
            'message': 'Unauthorized reminder',
            'time': next_week.isoformat()
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a reminder
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_reminder_retrieve_endpoint(self):
        """Test reminder retrieve endpoint"""
        url = reverse('reminder-detail', kwargs={'pk': self.reminder1.id})
        
        # Test owner can retrieve their reminder
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], "Doctor's appointment")
        self.assertEqual(response.data['baby'], self.baby1.id)
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_reminder_update_endpoint(self):
        """Test reminder update endpoint"""
        url = reverse('reminder-detail', kwargs={'pk': self.reminder1.id})
        
        # Get current time for updated reminder
        now = datetime.now(pytz.UTC)
        next_month = now + timedelta(days=30)
        
        # Test owner can update their reminder
        data = {
            'baby': self.baby1.id,
            'message': 'Updated appointment',
            'time': next_month.isoformat()
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Updated appointment')
        
        # Verify reminder was updated in database
        self.reminder1.refresh_from_db()
        self.assertEqual(self.reminder1.message, 'Updated appointment')
        
        # Test non-owner cannot update
        url = reverse('reminder-detail', kwargs={'pk': self.reminder2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_reminder_delete_endpoint(self):
        """Test reminder delete endpoint"""
        url = reverse('reminder-detail', kwargs={'pk': self.reminder1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Reminder.objects.filter(id=self.reminder1.id).count(), 1)
        
        # Test owner can delete their reminder
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify reminder was deleted from database
        self.assertEqual(Reminder.objects.filter(id=self.reminder1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('reminder-detail', kwargs={'pk': self.reminder2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Reminder.objects.filter(id=self.reminder2.id).count(), 1)

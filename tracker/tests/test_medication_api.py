from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Medication
from datetime import datetime, date
import pytz


class MedicationAPITestCase(TestCase):
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
        
        # Create medications for each user
        self.medication1 = Medication.objects.create(
            user=self.user1,
            name='Vitamin D',
            dosage='400 IU',
            frequency='daily',
            start_date='2023-01-15',
            end_date='2023-07-15'
        )
        
        self.medication2 = Medication.objects.create(
            user=self.user2,
            name='Iron Supplement',
            dosage='15 mg',
            frequency='daily',
            start_date='2023-02-01',
            end_date=None
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_medication_list_endpoint(self):
        """Test medication list endpoint"""
        url = reverse('medication-list')
        
        # Test authenticated user can list their medications
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Vitamin D')
        self.assertEqual(response.data[0]['dosage'], '400 IU')
        
        # Test second user can list their medications
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Iron Supplement')
        self.assertEqual(response.data[0]['dosage'], '15 mg')
        
        # Test unauthenticated user cannot list medications
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_medication_create_endpoint(self):
        """Test medication create endpoint"""
        url = reverse('medication-list')
        
        # Test authenticated user can create a medication
        data = {
            'name': 'Vitamin C',
            'dosage': '500 mg',
            'frequency': 'daily',
            'start_date': '2023-03-01',
            'end_date': '2023-09-01'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Vitamin C')
        self.assertEqual(response.data['dosage'], '500 mg')
        self.assertEqual(response.data['frequency'], 'daily')
        
        # Verify medication was created in database
        self.assertEqual(Medication.objects.filter(user=self.user1).count(), 2)
        
        # Test unauthenticated user cannot create a medication
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_medication_retrieve_endpoint(self):
        """Test medication retrieve endpoint"""
        url = reverse('medication-detail', kwargs={'pk': self.medication1.id})
        
        # Test owner can retrieve their medication
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Vitamin D')
        self.assertEqual(response.data['dosage'], '400 IU')
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_medication_update_endpoint(self):
        """Test medication update endpoint"""
        url = reverse('medication-detail', kwargs={'pk': self.medication1.id})
        
        # Test owner can update their medication
        data = {
            'name': 'Vitamin D3',
            'dosage': '800 IU',
            'frequency': 'daily',
            'start_date': '2023-01-15',
            'end_date': '2023-12-31'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Vitamin D3')
        self.assertEqual(response.data['dosage'], '800 IU')
        
        # Verify medication was updated in database
        self.medication1.refresh_from_db()
        self.assertEqual(self.medication1.name, 'Vitamin D3')
        self.assertEqual(self.medication1.dosage, '800 IU')
        
        # Test non-owner cannot update
        url = reverse('medication-detail', kwargs={'pk': self.medication2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_medication_delete_endpoint(self):
        """Test medication delete endpoint"""
        url = reverse('medication-detail', kwargs={'pk': self.medication1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Medication.objects.filter(id=self.medication1.id).count(), 1)
        
        # Test owner can delete their medication
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify medication was deleted from database
        self.assertEqual(Medication.objects.filter(id=self.medication1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('medication-detail', kwargs={'pk': self.medication2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Medication.objects.filter(id=self.medication2.id).count(), 1)

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Baby, DoctorAppointment
from datetime import datetime, timedelta
import pytz


class DoctorAppointmentAPITestCase(TestCase):
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
        
        # Get current time for doctor appointment records
        now = datetime.now(pytz.UTC)
        tomorrow = now + timedelta(days=1)
        next_week = now + timedelta(days=7)
        
        # Create doctor appointments for each user
        self.doctor_appointment1 = DoctorAppointment.objects.create(
            baby=self.baby1,
            doctor_name='Dr. Smith',
            date=tomorrow.date(),
            time=tomorrow.time(),
            notes='Regular checkup',
            location='Pediatric Clinic',
            reason='Regular checkup'
        )
        
        self.doctor_appointment2 = DoctorAppointment.objects.create(
            baby=self.baby2,
            doctor_name='Dr. Johnson',
            date=next_week.date(),
            time=next_week.time(),
            notes='Vaccination',
            location='Family Health Center',
            reason='Vaccination'
        )
        
        # Create API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        
        self.unauthenticated_client = APIClient()
    
    def test_doctor_appointment_list_endpoint(self):
        """Test doctor appointment list endpoint"""
        url = reverse('doctor-appointment-list')
        
        # Test authenticated user can list their doctor appointments
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby1.id)
        self.assertEqual(response.data[0]['doctor_name'], 'Dr. Smith')
        self.assertEqual(response.data[0]['location'], 'Pediatric Clinic')
        
        # Test second user can list their doctor appointments
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['baby'], self.baby2.id)
        self.assertEqual(response.data[0]['doctor_name'], 'Dr. Johnson')
        self.assertEqual(response.data[0]['location'], 'Family Health Center')
        
        # Test unauthenticated user cannot list doctor appointments
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_doctor_appointment_create_endpoint(self):
        """Test doctor appointment create endpoint"""
        url = reverse('doctor-appointment-list')
        
        # Get current time for new doctor appointment
        now = datetime.now(pytz.UTC)
        next_month = now + timedelta(days=30)
        
        # Test authenticated user can create a doctor appointment for their baby
        data = {
            'baby': self.baby1.id,
            'doctor_name': 'Dr. Wilson',
            'date': next_month.date().isoformat(),
            'time': next_month.time().isoformat(),
            'notes': 'Annual checkup',
            'location': 'Children\'s Hospital',
            'reason': 'Annual checkup'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['doctor_name'], 'Dr. Wilson')
        self.assertEqual(response.data['location'], 'Children\'s Hospital')
        
        # Verify doctor appointment was created in database
        self.assertEqual(DoctorAppointment.objects.filter(baby=self.baby1).count(), 2)
        
        # Test user cannot create doctor appointment for another user's baby
        data = {
            'baby': self.baby2.id,
            'doctor_name': 'Dr. Wilson',
            'date': next_month.date().isoformat(),
            'time': next_month.time().isoformat(),
            'notes': 'Unauthorized appointment',
            'location': 'Children\'s Hospital',
            'reason': 'Unauthorized appointment'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Test unauthenticated user cannot create a doctor appointment
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_doctor_appointment_retrieve_endpoint(self):
        """Test doctor appointment retrieve endpoint"""
        url = reverse('doctor-appointment-detail', kwargs={'pk': self.doctor_appointment1.id})
        
        # Test owner can retrieve their doctor appointment
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['baby'], self.baby1.id)
        self.assertEqual(response.data['doctor_name'], 'Dr. Smith')
        
        # Test non-owner cannot retrieve
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot retrieve
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_doctor_appointment_update_endpoint(self):
        """Test doctor appointment update endpoint"""
        url = reverse('doctor-appointment-detail', kwargs={'pk': self.doctor_appointment1.id})
        
        # Get current time for updated doctor appointment
        now = datetime.now(pytz.UTC)
        next_week = now + timedelta(days=7)
        
        # Test owner can update their doctor appointment
        data = {
            'baby': self.baby1.id,
            'doctor_name': 'Dr. Smith Jr.',
            'date': next_week.date().isoformat(),
            'time': next_week.time().isoformat(),
            'notes': 'Rescheduled checkup',
            'location': 'New Pediatric Clinic',
            'reason': 'Rescheduled checkup'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['doctor_name'], 'Dr. Smith Jr.')
        self.assertEqual(response.data['notes'], 'Rescheduled checkup')
        self.assertEqual(response.data['location'], 'New Pediatric Clinic')
        
        # Verify doctor appointment was updated in database
        self.doctor_appointment1.refresh_from_db()
        self.assertEqual(self.doctor_appointment1.doctor_name, 'Dr. Smith Jr.')
        self.assertEqual(self.doctor_appointment1.notes, 'Rescheduled checkup')
        self.assertEqual(self.doctor_appointment1.location, 'New Pediatric Clinic')
        
        # Test non-owner cannot update
        url = reverse('doctor-appointment-detail', kwargs={'pk': self.doctor_appointment2.id})
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_doctor_appointment_delete_endpoint(self):
        """Test doctor appointment delete endpoint"""
        url = reverse('doctor-appointment-detail', kwargs={'pk': self.doctor_appointment1.id})
        
        # Test non-owner cannot delete
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(DoctorAppointment.objects.filter(id=self.doctor_appointment1.id).count(), 1)
        
        # Test owner can delete their doctor appointment
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify doctor appointment was deleted from database
        self.assertEqual(DoctorAppointment.objects.filter(id=self.doctor_appointment1.id).count(), 0)
        
        # Test unauthenticated user cannot delete
        url = reverse('doctor-appointment-detail', kwargs={'pk': self.doctor_appointment2.id})
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(DoctorAppointment.objects.filter(id=self.doctor_appointment2.id).count(), 1)

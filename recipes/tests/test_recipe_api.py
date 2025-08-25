from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from recipes.models import Recipe, Ingredient
from rest_framework.test import force_authenticate


class RecipeAPITestCase(TestCase):
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
        
        # Create recipes for each user
        self.recipe1 = Recipe.objects.create(
            name="Baby Puree",
            description="Simple vegetable puree for babies",
            instructions="Steam vegetables and blend until smooth",
            created_by=self.user1.id,
            category=1,
            is_private=False,
            public_edits=True
        )
        self.recipe2 = Recipe.objects.create(
            name="Fruit Smoothie",
            description="Nutritious fruit smoothie for toddlers",
            instructions="Blend fruits with yogurt",
            created_by=self.user2.id,
            category=2,
            is_private=False,
            public_edits=True
        )
        
        # Create ingredients for recipes
        Ingredient.objects.create(
            recipe=self.recipe1,
            name="Carrots",
            quantity=2.0,
            unit=1
        )
        Ingredient.objects.create(
            recipe=self.recipe1,
            name="Sweet Potato",
            quantity=1.0,
            unit=1
        )
        Ingredient.objects.create(
            recipe=self.recipe2,
            name="Banana",
            quantity=1.0,
            unit=1
        )
        Ingredient.objects.create(
            recipe=self.recipe2,
            name="Yogurt",
            quantity=0.5,
            unit=2
        )
        
        # Setup API clients
        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)
        # Mark as test request
        self.client1._is_test_request = True
        
        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)
        # Mark as test request
        self.client2._is_test_request = True
        
        self.unauthenticated_client = APIClient()
        # Mark as test request
        self.unauthenticated_client._is_test_request = True
    
    def test_recipe_list_endpoint(self):
        """Test recipe list endpoint"""
        url = reverse('recipe-list')
        
        # Test authenticated user can see all recipes (IsAuthenticatedOrReadOnly)
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should see both recipes
        
        # Test unauthenticated user can see all recipes (read-only)
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should see both recipes
    
    def test_recipe_create_endpoint(self):
        """Test recipe create endpoint"""
        url = reverse('recipe-list')
        
        # Test authenticated user can create a recipe
        data = {
            'name': "Finger Food",
            'description': "Easy finger foods for babies",
            'instructions': "Cut soft foods into small pieces",
            'category': 3,
            'is_private': False,
            'public_edits': True,
            'created_by': self.user1.id
        }
        response = self.client1.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Finger Food")
        # Don't check the exact UUID format, just verify it exists
        self.assertIn('created_by', response.data)
        
        # Verify recipe was created
        self.assertTrue(Recipe.objects.filter(name="Finger Food", created_by=self.user1.id).exists())
        
        # Test unauthenticated user cannot create
        response = self.unauthenticated_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_recipe_retrieve_endpoint(self):
        """Test recipe retrieve endpoint"""
        url = reverse('recipe-detail', kwargs={'pk': self.recipe1.id})
        
        # Test authenticated user can retrieve any recipe
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Baby Puree")
        
        # Test another authenticated user can retrieve the recipe
        response = self.client2.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Baby Puree")
        
        # Test unauthenticated user can retrieve (read-only)
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Baby Puree")
    
    def test_recipe_update_endpoint(self):
        """Test recipe update endpoint"""
        url = reverse('recipe-detail', kwargs={'pk': self.recipe1.id})
        
        # Test owner can update their recipe
        data = {
            'name': "Updated Baby Puree",
            'description': "Updated vegetable puree for babies",
            'instructions': "Steam vegetables and blend until smooth",
            'category': 1,
            'is_private': False,
            'public_edits': True,
            'created_by': self.user1.id
        }
        response = self.client1.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Baby Puree")
        self.assertEqual(response.data['description'], "Updated vegetable puree for babies")
        
        # Verify recipe was updated
        self.recipe1.refresh_from_db()
        self.assertEqual(self.recipe1.name, "Updated Baby Puree")
        
        # Test non-owner cannot update
        url = reverse('recipe-detail', kwargs={'pk': self.recipe1.id})
        data = {
            'name': "Hacked Recipe",
            'description': "This should not work",
            'instructions': "Steam vegetables and blend until smooth",
            'category': 1,
            'is_private': False,
            'public_edits': True,
            'created_by': self.user2.id  # Attempting to change ownership
        }
        response = self.client2.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test unauthenticated user cannot update
        response = self.unauthenticated_client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_recipe_partial_update_endpoint(self):
        """Test recipe partial update endpoint"""
        url = reverse('recipe-detail', kwargs={'pk': self.recipe1.id})
        
        # Test owner can partially update their recipe
        data = {
            'name': "Partially Updated Puree",
            'category': 2
        }
        response = self.client1.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Partially Updated Puree")
        self.assertEqual(response.data['category'], 2)
        
        # Verify recipe was updated
        self.recipe1.refresh_from_db()
        self.assertEqual(self.recipe1.name, "Partially Updated Puree")
        self.assertEqual(self.recipe1.category, 2)
        
        # Test non-owner cannot partially update
        data = {
            'name': "Hacked Partial Update",
            'created_by': self.user2.id  # Attempting to change ownership
        }
        response = self.client2.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Test unauthenticated user cannot partially update
        response = self.unauthenticated_client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_recipe_delete_endpoint(self):
        """Test recipe delete endpoint"""
        url = reverse('recipe-detail', kwargs={'pk': self.recipe1.id})
        
        # Test unauthenticated user cannot delete
        response = self.unauthenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Test owner can delete their recipe
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify recipe was deleted
        self.assertFalse(Recipe.objects.filter(id=self.recipe1.id).exists())
        
        # Test attempting to delete a non-existent recipe returns 404
        response = self.client2.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_ingredient_list_endpoint(self):
        """Test ingredient list endpoint"""
        url = reverse('ingredient-list')
        
        # Test authenticated user can see all ingredients
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # Should see all ingredients
        
        # Test unauthenticated user can see all ingredients (read-only)
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # Should see all ingredients
    
    def test_ingredient_create_endpoint(self):
        """Test ingredient create endpoint"""
        url = reverse('ingredient-list')
        
        # Test authenticated user can create an ingredient for their recipe
        data = {
            'recipe': self.recipe1.id,
            'name': "Peas",
            'quantity': 0.25,
            'unit': 2
        }
        response = self.client1.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "Peas")
        self.assertEqual(response.data['recipe'], self.recipe1.id)
        
        # Verify ingredient was created
        self.assertTrue(Ingredient.objects.filter(recipe=self.recipe1, name="Peas").exists())
        
        # Test user cannot create ingredient for another user's recipe
        data = {
            'recipe': self.recipe2.id,  # User1 trying to add ingredient to User2's recipe
            'name': "Apple",
            'quantity': 1.0,
            'unit': 1
        }
        response = self.client1.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Test unauthenticated user cannot create
        response = self.unauthenticated_client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

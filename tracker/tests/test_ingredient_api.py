from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tracker.models import Recipe, Ingredient


class IngredientAPITestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1', email='test1@example.com', password='testpassword1'
        )
        self.user2 = User.objects.create_user(
            username='testuser2', email='test2@example.com', password='testpassword2'
        )

        self.recipe1 = Recipe.objects.create(
            name='Sweet Potato Puree',
            instructions='Blend it.',
            user=self.user1
        )
        self.recipe2 = Recipe.objects.create(
            name='Apple Mash',
            instructions='Mash it.',
            user=self.user2
        )

        self.ingredient1 = Ingredient.objects.create(
            name='Sweet Potato', recipe=self.recipe1, quantity=2.0, unit='cups'
        )
        self.ingredient2 = Ingredient.objects.create(
            name='Apple', recipe=self.recipe2, quantity=1.0, unit='pieces'
        )

        self.client1 = APIClient()
        self.client1.force_authenticate(user=self.user1)

        self.client2 = APIClient()
        self.client2.force_authenticate(user=self.user2)

        self.unauthenticated_client = APIClient()

    def test_ingredient_list_returns_only_own_ingredients(self):
        url = reverse('ingredient-list')
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Sweet Potato')

    def test_ingredient_list_unauthenticated(self):
        url = reverse('ingredient-list')
        response = self.unauthenticated_client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ingredient_create(self):
        url = reverse('ingredient-list')
        data = {
            'name': 'Butter',
            'recipe': self.recipe1.id,
            'quantity': 1.0,
            'unit': 'tbsp'
        }
        response = self.client1.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Butter')
        self.assertEqual(Ingredient.objects.filter(recipe=self.recipe1).count(), 2)

    def test_ingredient_create_unauthenticated(self):
        url = reverse('ingredient-list')
        data = {'name': 'Butter', 'recipe': self.recipe1.id, 'quantity': 1.0, 'unit': 'tbsp'}
        response = self.unauthenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_ingredient_retrieve(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient1.id})
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Sweet Potato')

    def test_ingredient_retrieve_other_users_ingredient_returns_404(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient2.id})
        response = self.client1.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_ingredient_update(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient1.id})
        data = {
            'name': 'Sweet Potato Updated',
            'recipe': self.recipe1.id,
            'quantity': 3.0,
            'unit': 'cups'
        }
        response = self.client1.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Sweet Potato Updated')
        self.ingredient1.refresh_from_db()
        self.assertEqual(self.ingredient1.quantity, 3.0)

    def test_ingredient_partial_update(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient1.id})
        response = self.client1.patch(url, {'quantity': 5.0})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ingredient1.refresh_from_db()
        self.assertEqual(self.ingredient1.quantity, 5.0)

    def test_ingredient_delete(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient1.id})
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ingredient.objects.filter(id=self.ingredient1.id).count(), 0)

    def test_ingredient_delete_other_users_returns_404(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient2.id})
        response = self.client1.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Ingredient.objects.filter(id=self.ingredient2.id).count(), 1)

    def test_ingredient_update_unauthenticated(self):
        url = reverse('ingredient-detail', kwargs={'pk': self.ingredient1.id})
        response = self.unauthenticated_client.put(url, {'name': 'Hack', 'recipe': self.recipe1.id, 'quantity': 1, 'unit': 'g'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

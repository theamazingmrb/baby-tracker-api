from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView, IngredientListCreateView, FavoriteListCreateView

urlpatterns = [
    path("", RecipeListCreateView.as_view(), name="recipe-list"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("ingredients/", IngredientListCreateView.as_view(), name="ingredient-list"),
    path("favorites/", FavoriteListCreateView.as_view(), name="favorite-list"),
]

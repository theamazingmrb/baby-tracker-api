from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    cover_image = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField()
    created_by = models.UUIDField()
    category = models.BigIntegerField()
    is_private = models.BooleanField(default=False)
    public_edits = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    quantity = models.FloatField()
    unit = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.name}"

class Favorite(models.Model):
    id = models.BigAutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="favorites")
    user_id = models.UUIDField()

    def __str__(self):
        return f"Recipe {self.recipe_id} favorited by {self.user_id}"

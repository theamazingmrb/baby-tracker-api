from rest_framework import serializers
from .models import Baby, Feeding, DiaperChange, Sleep, Reminder, GrowthMilestone, Medication, DoctorAppointment, PumpingSession, Milestone, Recipe, Ingredient
from django.contrib.auth.models import User

class BabyInsightSerializer(serializers.Serializer):
    feeding_insights = serializers.JSONField(required=False)
    sleep_insights = serializers.JSONField(required=False)
    growth_insights = serializers.JSONField(required=False)
    diaper_insights = serializers.JSONField(required=False)
    comprehensive_insights = serializers.JSONField(required=False)

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = ['id', 'name', 'birth_date', 'gender', 'user']
        read_only_fields = ['user']

class BabyStatsSerializer(serializers.Serializer):
    height = serializers.FloatField()
    weight = serializers.FloatField()
    age_months = serializers.IntegerField()

class FeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeding
        fields = "__all__"

class DiaperChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaperChange
        fields = "__all__"

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = "__all__"

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
        read_only_fields = ['user']

class GrowthMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthMilestone
        fields = "__all__"

class PumpingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpingSession
        fields = "__all__"
        read_only_fields = ['user']

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointment
        fields = "__all__"

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"
        read_only_fields = ['user']

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'cover_image', 'description', 'instructions', 'category', 'is_private', 'user']
        read_only_fields = ['user']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"
from rest_framework import serializers
from .models import Baby, Feeding, DiaperChange, Sleep, Reminder, GrowthMilestone, Medication, DoctorAppointment, PumpingSession, Milestone
from django.core.exceptions import PermissionDenied

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
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and hasattr(value, 'user') and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value

class DiaperChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiaperChange
        fields = "__all__"
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value

class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = "__all__"
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = "__all__"
        read_only_fields = ['user']
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value

class GrowthMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthMilestone
        fields = "__all__"
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value

class PumpingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpingSession
        fields = "__all__"
        read_only_fields = ['user']
        
    def validate(self, data):
        # Ensure the user has permission to create/update this resource
        request = self.context.get('request')
        if request and request.user and hasattr(self.instance, 'user') and self.instance.user != request.user:
            raise serializers.ValidationError("You don't have permission to modify this resource.")
        return data

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointment
        fields = "__all__"
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"
        read_only_fields = ['user']
        
    def validate(self, data):
        # Ensure the user has permission to create/update this resource
        request = self.context.get('request')
        if request and request.user and hasattr(self.instance, 'user') and self.instance.user != request.user:
            raise serializers.ValidationError("You don't have permission to modify this resource.")
        return data

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'
        
    def validate_baby(self, value):
        # Ensure the baby belongs to the current user
        request = self.context.get('request')
        if request and request.user and value.user != request.user:
            raise serializers.ValidationError("You don't have permission to add data for this baby.")
        return value
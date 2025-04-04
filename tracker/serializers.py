from rest_framework import serializers
from .models import Baby, Feeding, DiaperChange, Sleep, Reminder, GrowthMilestone, Medication, DoctorAppointment, PumpingSession, Milestone

class BabyInsightSerializer(serializers.Serializer):
    feeding_insights = serializers.JSONField()
    sleep_insights = serializers.JSONField()

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

class GrowthMilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthMilestone
        fields = "__all__"

class PumpingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PumpingSession
        fields = "__all__"

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointment
        fields = "__all__"

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"

class MilestoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = '__all__'
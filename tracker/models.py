from django.db import models
from django.contrib.auth.models import User
from .enums import FeedingSideEnum, PumpingSideEnum

class Baby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Feeding(models.Model):
    FEEDING_TYPES = [
        ("breastfeeding", "Breastfeeding"),
        ("bottle", "Bottle"),
        ("solid", "Solid Food"),
    ]

    FEEDING_SIDE_CHOICES = [
        ("left_feeding", "Left"),
        ("right_feeding", "Right"),
        ("both_feeding", "Both"),
    ]
        
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="feedings")
    time = models.DateTimeField(auto_now_add=True)
    feeding_type = models.CharField(max_length=20, choices=FEEDING_TYPES)
    quantity = models.FloatField(help_text="Amount in ounces/ml")
    last_side = models.CharField(
        max_length=15,
        choices=FeedingSideEnum.choices(),  # Correct: Call choices() method
        null=True,
        blank=True
    )
    def __str__(self):
        return f"{self.baby.name} - {self.feeding_type} at {self.time}"

class DiaperChange(models.Model):
    DIAPER_TYPES = [
        ("wet", "Wet"),
        ("dirty", "Dirty"),
        ("mixed", "Mixed"),
    ]
    
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="diaper_changes")
    time = models.DateTimeField(auto_now_add=True)
    diaper_type = models.CharField(max_length=10, choices=DIAPER_TYPES)

    def __str__(self):
        return f"{self.baby.name} - {self.diaper_type} diaper at {self.time}"

class Sleep(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="sleep_sessions")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.baby.name} - Sleep from {self.start_time} to {self.end_time or 'ongoing'}"

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="reminders")
    message = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.baby.name}: {self.message} at {self.time}"

class GrowthMilestone(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="growth_milestones")
    date = models.DateField()
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.baby.name} - {self.height} cm, {self.weight} kg on {self.date}"

class Milestone(models.Model):
    MILESTONE_CATEGORIES = [
        ("physical", "Physical"),
        ("social", "Social"),
        ("cognitive", "Cognitive"),
        ("language", "Language"),
        ("emotional", "Emotional"),
    ]
    
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="milestones")
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=MILESTONE_CATEGORIES)
    date_achieved = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.baby.name} - {self.title} ({self.category}) on {self.date_achieved}"

class PumpingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pumping_sessions")
    time = models.DateTimeField(auto_now_add=True)
    PUMPING_SIDE_CHOICES = [
        ("left_pump", "Left"),
        ("right_pump", "Right"),
        ("both_pump", "Both"),
    ]

    side = models.CharField(
        max_length=15,
        choices=PumpingSideEnum.choices(),
    )  
    quantity = models.FloatField(help_text="Milk pumped in ounces/ml")

    def __str__(self):
        return f"{self.user.username} - {self.quantity} oz/ml pumped at {self.time}"


class DoctorAppointment(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="appointments")
    doctor_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.baby.name} - {self.doctor_name} on {self.date}"


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="medications")
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=50, choices=[("daily", "Daily"), ("weekly", "Weekly"), ("as_needed", "As Needed")])
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.name} ({self.dosage})"

from django.db import models
from django.contrib.auth.models import User
from .enums import FeedingSideEnum, PumpingSideEnum

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    instructions = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    category = models.CharField(max_length=100, default="baby food")
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")
    quantity = models.FloatField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.name}"

class Baby(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True) 
    name = models.CharField(max_length=100)
    birth_date = models.DateField(db_index=True)
    gender = models.CharField(max_length=10)

    class Meta:
        indexes = [
            models.Index(fields=['user', 'name']),
            models.Index(fields=['user', 'birth_date']),
        ]

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
        
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="feedings", db_index=True)
    time = models.DateTimeField(auto_now_add=True, db_index=True)
    feeding_type = models.CharField(max_length=20, choices=FEEDING_TYPES)
    quantity = models.FloatField(help_text="Amount in ounces/ml")
    last_side = models.CharField(
        max_length=15,
        choices=FeedingSideEnum.choices(),
        null=True,
        blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=['baby', 'time']),
            models.Index(fields=['baby', 'feeding_type']),
        ]

    def __str__(self):
        return f"{self.baby.name} - {self.feeding_type} at {self.time}"

class DiaperChange(models.Model):
    DIAPER_TYPES = [
        ("wet", "Wet"),
        ("dirty", "Dirty"),
        ("mixed", "Mixed"),
    ]
    
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="diaper_changes", db_index=True)
    time = models.DateTimeField(auto_now_add=True, db_index=True)
    diaper_type = models.CharField(max_length=10, choices=DIAPER_TYPES)

    class Meta:
        indexes = [
            models.Index(fields=['baby', 'time']),
            models.Index(fields=['baby', 'diaper_type']),
        ]

    def __str__(self):
        return f"{self.baby.name} - {self.diaper_type} diaper at {self.time}"

class Sleep(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="sleep_sessions", db_index=True)
    start_time = models.DateTimeField(db_index=True)
    end_time = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['baby', 'start_time']),
            models.Index(fields=['baby', 'end_time']),
        ]

    def __str__(self):
        return f"{self.baby.name} - Sleep from {self.start_time} to {self.end_time or 'ongoing'}"

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reminders")
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="reminders")
    message = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return f"Reminder for {self.baby.name}: {self.message} at {self.time}"

class GrowthMeasurement(models.Model):
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="growth_measurements")
    date = models.DateField()
    height = models.FloatField(help_text="Height in cm")
    weight = models.FloatField(help_text="Weight in kg")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.baby.name} - {self.height} cm, {self.weight} kg on {self.date}"

class DevelopmentalMilestone(models.Model):
    MILESTONE_CATEGORIES = [
        ("physical", "Physical"),
        ("social", "Social"),
        ("cognitive", "Cognitive"),
        ("language", "Language"),
        ("emotional", "Emotional"),
    ]
    
    baby = models.ForeignKey(Baby, on_delete=models.CASCADE, related_name="developmental_milestones")
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

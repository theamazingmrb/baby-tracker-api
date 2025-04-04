from django.urls import path
from .views import (
    BabyListCreateView, BabyDetailView, BabyStatsView,
    FeedingListCreateView, FeedingDetailView,
    DiaperChangeListCreateView, SleepListCreateView,
    ReminderListCreateView, GrowthMilestoneListCreateView, BabyAIInsightsView,
    MedicationListCreateView, MedicationDeleteView,
    PumpingSessionListCreateView, PumpingSessionDeleteView,
    DoctorAppointmentListCreateView, DoctorAppointmentDeleteView,
    RegisterView,
    MilestoneListCreateView, MilestoneDetailView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("babies/", BabyListCreateView.as_view(), name="baby-list"),
    path("babies/<int:pk>/", BabyDetailView.as_view(), name="baby-detail"),
    path("babies/stats/", BabyStatsView.as_view(), name="baby-stats"),
    
    path("feedings/", FeedingListCreateView.as_view(), name="feeding-list"),
    path("feedings/<int:pk>/", FeedingDetailView.as_view(), name="feeding-detail"),

    path("diaper-changes/", DiaperChangeListCreateView.as_view(), name="diaper-change-list"),

    path("sleep/", SleepListCreateView.as_view(), name="sleep-list"),

    path("reminders/", ReminderListCreateView.as_view(), name="reminder-list"),

    path("growth-milestones/", GrowthMilestoneListCreateView.as_view(), name="growth-milestone-list"),

    path("babies/ai-insights/", BabyAIInsightsView.as_view(), name="baby-ai-insights"),

    
    path("medications/", MedicationListCreateView.as_view(), name="medication-list"),
    path("medications/<int:pk>/", MedicationDeleteView.as_view(), name="medication-delete"),

    path("pumping-sessions/", PumpingSessionListCreateView.as_view(), name="pumping-session-list"),
    path("pumping-sessions/<int:pk>/", PumpingSessionDeleteView.as_view(), name="pumping-session-delete"),

    path("appointments/", DoctorAppointmentListCreateView.as_view(), name="doctor-appointment-list"),
    path("appointments/<int:pk>/", DoctorAppointmentDeleteView.as_view(), name="doctor-appointment-delete"),

    path("babies/<int:baby_id>/milestones/", MilestoneListCreateView.as_view(), name='milestone-list'),
    path("babies/<int:baby_id>/milestones/<int:pk>/", MilestoneDetailView.as_view(), name='milestone-detail'),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

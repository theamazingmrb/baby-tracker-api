from django.urls import path
from .views import (
    BabyListCreateView, BabyDetailView, BabyStatsView,
    FeedingListCreateView, FeedingDetailView,
    DiaperChangeListCreateView, DiaperChangeDetailView, SleepListCreateView, SleepDetailView,
    ReminderListCreateView, ReminderDetailView, GrowthMilestoneListCreateView, GrowthMilestoneDetailView, BabyAIInsightsView,
    MedicationListCreateView, MedicationDetailView,
    PumpingSessionListCreateView, PumpingSessionDetailView,
    DoctorAppointmentListCreateView, DoctorAppointmentDetailView,
    RegisterView,
    MilestoneListCreateView, MilestoneDetailView,
    InsightsVisualizationView
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
    path("diaper-changes/<int:pk>/", DiaperChangeDetailView.as_view(), name="diaper-change-detail"),

    path("sleep/", SleepListCreateView.as_view(), name="sleep-list"),
    path("sleep/<int:pk>/", SleepDetailView.as_view(), name="sleep-detail"),

    path("reminders/", ReminderListCreateView.as_view(), name="reminder-list"),
    path("reminders/<int:pk>/", ReminderDetailView.as_view(), name="reminder-detail"),

    path("growth-milestones/", GrowthMilestoneListCreateView.as_view(), name="growth-milestone-list"),
    path("growth-milestones/<int:pk>/", GrowthMilestoneDetailView.as_view(), name="growth-milestone-detail"),

    path("babies/<int:baby_id>/ai-insights/", BabyAIInsightsView.as_view(), name="baby-ai-insights"),
    path("babies/<int:baby_id>/visualizations/", InsightsVisualizationView.as_view(), name="baby-insights-visualizations"),

    
    path("medications/", MedicationListCreateView.as_view(), name="medication-list"),
    path("medications/<int:pk>/", MedicationDetailView.as_view(), name="medication-detail"),

    path("pumping-sessions/", PumpingSessionListCreateView.as_view(), name="pumping-session-list"),
    path("pumping-sessions/<int:pk>/", PumpingSessionDetailView.as_view(), name="pumping-session-detail"),

    path("appointments/", DoctorAppointmentListCreateView.as_view(), name="doctor-appointment-list"),
    path("appointments/<int:pk>/", DoctorAppointmentDetailView.as_view(), name="doctor-appointment-detail"),

    path("babies/<int:baby_id>/milestones/", MilestoneListCreateView.as_view(), name='milestone-list'),
    path("babies/<int:baby_id>/milestones/<int:pk>/", MilestoneDetailView.as_view(), name='milestone-detail'),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

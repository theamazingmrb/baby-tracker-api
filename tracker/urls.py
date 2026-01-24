from django.urls import path
from .views import (
    BabyListCreateView, BabyDetailView, BabyStatsView,
    FeedingListCreateView, FeedingDetailView,
    DiaperChangeListCreateView, DiaperChangeDetailView, SleepListCreateView, SleepDetailView,
    ReminderListCreateView, ReminderDetailView, GrowthMeasurementListCreateView, GrowthMeasurementDetailView, BabyAIInsightsView,
    MedicationListCreateView, MedicationDetailView,
    PumpingSessionListCreateView, PumpingSessionDetailView,
    DoctorAppointmentListCreateView, DoctorAppointmentDetailView,
    RegisterView,
    DevelopmentalMilestoneListCreateView, DevelopmentalMilestoneDetailView,
    InsightsVisualizationView,
    RecipeListCreateView, RecipeDetailView,
    IngredientListCreateView, IngredientDetailView
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

    path("growth-measurements/", GrowthMeasurementListCreateView.as_view(), name="growth-measurement-list"),
    path("growth-measurements/<int:pk>/", GrowthMeasurementDetailView.as_view(), name="growth-measurement-detail"),

    path("babies/<int:baby_id>/ai-insights/", BabyAIInsightsView.as_view(), name="baby-ai-insights"),
    path("babies/<int:baby_id>/visualizations/", InsightsVisualizationView.as_view(), name="baby-insights-visualizations"),

    
    path("medications/", MedicationListCreateView.as_view(), name="medication-list"),
    path("medications/<int:pk>/", MedicationDetailView.as_view(), name="medication-detail"),

    path("pumping-sessions/", PumpingSessionListCreateView.as_view(), name="pumping-session-list"),
    path("pumping-sessions/<int:pk>/", PumpingSessionDetailView.as_view(), name="pumping-session-detail"),

    path("appointments/", DoctorAppointmentListCreateView.as_view(), name="doctor-appointment-list"),
    path("appointments/<int:pk>/", DoctorAppointmentDetailView.as_view(), name="doctor-appointment-detail"),

    path("babies/<int:baby_id>/developmental-milestones/", DevelopmentalMilestoneListCreateView.as_view(), name='developmental-milestone-list'),
    path("babies/<int:baby_id>/developmental-milestones/<int:pk>/", DevelopmentalMilestoneDetailView.as_view(), name='developmental-milestone-detail'),

    path("recipes/", RecipeListCreateView.as_view(), name='recipe-list'),
    path("recipes/<int:pk>/", RecipeDetailView.as_view(), name='recipe-detail'),

    path("ingredients/", IngredientListCreateView.as_view(), name='ingredient-list'),
    path("ingredients/<int:pk>/", IngredientDetailView.as_view(), name='ingredient-detail'),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

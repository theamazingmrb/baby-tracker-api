from rest_framework import generics
from .models import Baby,Feeding,DiaperChange,Sleep,Reminder,GrowthMilestone, Milestone
from .serializers import BabySerializer,BabyInsightSerializer ,FeedingSerializer,DiaperChangeSerializer,SleepSerializer,ReminderSerializer,GrowthMilestoneSerializer,PumpingSessionSerializer,DoctorAppointmentSerializer,MedicationSerializer,BabyStatsSerializer, MilestoneSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.models import Count, Avg, Sum
from datetime import timedelta, date
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .ai_insights import AIInsights
from rest_framework_simplejwt.tokens import RefreshToken

class BabyListCreateView(generics.ListCreateAPIView):
    serializer_class = BabySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Baby.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BabyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Baby.objects.all()
    serializer_class = BabySerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        
        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        
        return Response({
            "message": "User created successfully",
            "tokens": {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }
        }, status=status.HTTP_201_CREATED)

class FeedingListCreateView(generics.ListCreateAPIView):
    queryset = Feeding.objects.all()
    serializer_class = FeedingSerializer
    permission_classes = [permissions.IsAuthenticated]

class FeedingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feeding.objects.all()
    serializer_class = FeedingSerializer
    permission_classes = [permissions.IsAuthenticated]

class DiaperChangeListCreateView(generics.ListCreateAPIView):
    queryset = DiaperChange.objects.all()
    serializer_class = DiaperChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

class SleepListCreateView(generics.ListCreateAPIView):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReminderListCreateView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

class GrowthMilestoneListCreateView(generics.ListCreateAPIView):
    queryset = GrowthMilestone.objects.all()
    serializer_class = GrowthMilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]


class BabyStatsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BabyStatsSerializer
    def get(self, request, baby_id):
        try:
            baby = Baby.objects.get(id=baby_id, user=request.user)
        except Baby.DoesNotExist:
            return Response({"error": "Baby not found"}, status=404)

        today = date.today()
        feedings_today = Feeding.objects.filter(baby=baby, time__date=today).count()

        avg_feed_interval = Feeding.objects.filter(baby=baby).aggregate(
            avg_time=Avg("time")
        )["avg_time"]

        sleep_sessions = Sleep.objects.filter(baby=baby, start_time__gte=today - timedelta(days=7))
        total_sleep_seconds = sum(
            (s.end_time - s.start_time).total_seconds() for s in sleep_sessions if s.end_time
        )
        total_sleep_hours = round(total_sleep_seconds / 3600, 2)

        return Response({
            "feedings_today": feedings_today,
            "avg_feeding_interval": avg_feed_interval,
            "total_sleep_hours": total_sleep_hours,
        })


class PumpingSessionListCreateView(generics.ListCreateAPIView):
    serializer_class = PumpingSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PumpingSession.objects.filter(user=self.request.user)

class PumpingSessionDeleteView(generics.DestroyAPIView):
    serializer_class = PumpingSessionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PumpingSession.objects.filter(user=self.request.user)

class DoctorAppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorAppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DoctorAppointment.objects.filter(baby__user=self.request.user)

class DoctorAppointmentDeleteView(generics.DestroyAPIView):
    serializer_class = DoctorAppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return DoctorAppointment.objects.filter(baby__user=self.request.user)

class MedicationListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

class MedicationDeleteView(generics.DestroyAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

class MilestoneListCreateView(generics.ListCreateAPIView):
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Milestone.objects.filter(baby__user=self.request.user)

class MilestoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MilestoneSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Milestone.objects.filter(baby__user=self.request.user)

class BabyAIInsightsView(APIView):
    serializer_class = BabyInsightSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, baby_id):
        try:
            baby = Baby.objects.get(id=baby_id, user=request.user)
        except Baby.DoesNotExist:
            return Response({"error": "Baby not found"}, status=404)

        ai = AIInsights(baby)
        feeding_insights = ai.get_feeding_insights()
        sleep_insights = ai.get_sleep_insights()

        return Response({
            "feeding_insights": feeding_insights,
            "sleep_insights": sleep_insights,
        })

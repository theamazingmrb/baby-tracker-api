from rest_framework import generics
from .models import Baby,Feeding,DiaperChange,Sleep,Reminder,GrowthMilestone, Milestone, PumpingSession, DoctorAppointment, Medication
from .serializers import BabySerializer,BabyInsightSerializer ,FeedingSerializer,DiaperChangeSerializer,SleepSerializer,ReminderSerializer,GrowthMilestoneSerializer,PumpingSessionSerializer,DoctorAppointmentSerializer,MedicationSerializer,BabyStatsSerializer, MilestoneSerializer, RegisterSerializer
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
from .permissions import IsTenantUser

class BabyListCreateView(generics.ListCreateAPIView):
    serializer_class = BabySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Baby.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BabyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BabySerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Baby.objects.filter(user=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class FeedingListCreateView(generics.ListCreateAPIView):
    serializer_class = FeedingSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Feeding.objects.filter(baby__user=self.request.user)
        
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(baby=baby)
            except Baby.DoesNotExist:
                raise permissions.exceptions.PermissionDenied("You don't have permission to add data for this baby.")
        else:
            serializer.save()

class FeedingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeedingSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Feeding.objects.filter(baby__user=self.request.user)

class DiaperChangeListCreateView(generics.ListCreateAPIView):
    serializer_class = DiaperChangeSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return DiaperChange.objects.filter(baby__user=self.request.user)
        
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(baby=baby)
            except Baby.DoesNotExist:
                raise permissions.exceptions.PermissionDenied("You don't have permission to add data for this baby.")
        else:
            serializer.save()

class DiaperChangeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiaperChangeSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return DiaperChange.objects.filter(baby__user=self.request.user)

class SleepListCreateView(generics.ListCreateAPIView):
    serializer_class = SleepSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Sleep.objects.filter(baby__user=self.request.user)
        
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(baby=baby)
            except Baby.DoesNotExist:
                raise permissions.exceptions.PermissionDenied("You don't have permission to add data for this baby.")
        else:
            serializer.save()

class SleepDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SleepSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Sleep.objects.filter(baby__user=self.request.user)

class ReminderListCreateView(generics.ListCreateAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(user=self.request.user, baby=baby)
            except Baby.DoesNotExist:
                raise permissions.exceptions.PermissionDenied("You don't have permission to add data for this baby.")
        else:
            serializer.save(user=self.request.user)

class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReminderSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return Reminder.objects.filter(user=self.request.user)

class GrowthMilestoneListCreateView(generics.ListCreateAPIView):
    serializer_class = GrowthMilestoneSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return GrowthMilestone.objects.filter(baby__user=self.request.user)
        
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(baby=baby)
            except Baby.DoesNotExist:
                raise permissions.exceptions.PermissionDenied("You don't have permission to add data for this baby.")
        else:
            serializer.save()

class GrowthMilestoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GrowthMilestoneSerializer
    permission_classes = [IsTenantUser]
    
    def get_queryset(self):
        return GrowthMilestone.objects.filter(baby__user=self.request.user)


class BabyStatsView(APIView):
    permission_classes = [IsTenantUser]
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
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return PumpingSession.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PumpingSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PumpingSessionSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return PumpingSession.objects.filter(user=self.request.user)

class DoctorAppointmentListCreateView(generics.ListCreateAPIView):
    serializer_class = DoctorAppointmentSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return DoctorAppointment.objects.filter(baby__user=self.request.user)

class DoctorAppointmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DoctorAppointmentSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return DoctorAppointment.objects.filter(baby__user=self.request.user)

class MedicationListCreateView(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MedicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

class MilestoneListCreateView(generics.ListCreateAPIView):
    serializer_class = MilestoneSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return Milestone.objects.filter(baby__user=self.request.user)

class MilestoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MilestoneSerializer
    permission_classes = [IsTenantUser]

    def get_queryset(self):
        return Milestone.objects.filter(baby__user=self.request.user)

class BabyAIInsightsView(APIView):
    serializer_class = BabyInsightSerializer
    permission_classes = [IsTenantUser]

    def get(self, request, baby_id):
        try:
            baby = Baby.objects.get(id=baby_id, user=request.user)
        except Baby.DoesNotExist:
            return Response({"error": "Baby not found"}, status=404)

        insight_type = request.query_params.get('type', 'all')
        ai = AIInsights(baby)
        
        if insight_type == 'feeding':
            return Response({
                "feeding_insights": ai.get_feeding_insights()
            })
        elif insight_type == 'sleep':
            return Response({
                "sleep_insights": ai.get_sleep_insights()
            })
        elif insight_type == 'growth':
            return Response({
                "growth_insights": ai.get_growth_insights()
            })
        elif insight_type == 'diaper':
            return Response({
                "diaper_insights": ai.get_diaper_insights()
            })
        elif insight_type == 'comprehensive':
            return Response({
                "comprehensive_insights": ai.get_comprehensive_insights()
            })
        else:  # 'all'
            feeding_insights = ai.get_feeding_insights()
            sleep_insights = ai.get_sleep_insights()
            growth_insights = ai.get_growth_insights()
            diaper_insights = ai.get_diaper_insights()
            comprehensive_insights = ai.get_comprehensive_insights()
            
            return Response({
                "feeding_insights": feeding_insights,
                "sleep_insights": sleep_insights,
                "growth_insights": growth_insights,
                "diaper_insights": diaper_insights,
                "comprehensive_insights": comprehensive_insights
            })
            
    def post(self, request, baby_id):
        try:
            baby = Baby.objects.get(id=baby_id, user=request.user)
        except Baby.DoesNotExist:
            return Response({"error": "Baby not found"}, status=404)
            
        # Generate report based on request data
        # For now, we'll return the same data as the GET method with type=all
        ai = AIInsights(baby)
        
        feeding_insights = ai.get_feeding_insights()
        sleep_insights = ai.get_sleep_insights()
        growth_insights = ai.get_growth_insights()
        diaper_insights = ai.get_diaper_insights()
        comprehensive_insights = ai.get_comprehensive_insights()
        
        return Response({
            "feeding_insights": feeding_insights,
            "sleep_insights": sleep_insights,
            "growth_insights": growth_insights,
            "diaper_insights": diaper_insights,
            "comprehensive_insights": comprehensive_insights
        })


class InsightsVisualizationView(APIView):
    permission_classes = [IsTenantUser]
    serializer_class = BabyInsightSerializer
    
    def get(self, request, baby_id):
        try:
            baby = Baby.objects.get(id=baby_id, user=request.user)
        except Baby.DoesNotExist:
            return Response({"error": "Baby not found"}, status=404)
            
        visualization_type = request.query_params.get('type', 'all')
        ai = AIInsights(baby)
        
        # Extract only visualization data from insights
        if visualization_type == 'feeding':
            insights = ai.get_feeding_insights()
            visualization_data = {
                'feeding_patterns': insights.get('patterns', {}),
                'feeding_trends': insights.get('trends', {}),
                'feeding_visualization': insights.get('visualization_data', {})
            }
            
        elif visualization_type == 'sleep':
            insights = ai.get_sleep_insights()
            visualization_data = {
                'sleep_patterns': insights.get('patterns', {}),
                'sleep_clusters': insights.get('clusters', {}),
                'sleep_visualization': insights.get('visualization_data', {})
            }
            
        elif visualization_type == 'growth':
            insights = ai.get_growth_insights()
            visualization_data = {
                'growth_trends': insights.get('growth_velocity', {}),
                'growth_visualization': insights.get('visualization_data', {})
            }
            
        elif visualization_type == 'diaper':
            insights = ai.get_diaper_insights()
            visualization_data = {
                'diaper_distribution': insights.get('type_distribution', {}),
                'diaper_visualization': insights.get('visualization_data', {})
            }
            
        else:  # Combined visualizations
            feeding_insights = ai.get_feeding_insights()
            sleep_insights = ai.get_sleep_insights()
            growth_insights = ai.get_growth_insights()
            diaper_insights = ai.get_diaper_insights()
            
            visualization_data = {
                'feeding': {
                    'patterns': feeding_insights.get('patterns', {}),
                    'visualization_data': feeding_insights.get('visualization_data', {})
                },
                'sleep': {
                    'patterns': sleep_insights.get('patterns', {}),
                    'visualization_data': sleep_insights.get('visualization_data', {})
                },
                'growth': {
                    'trends': growth_insights.get('growth_velocity', {}),
                    'visualization_data': growth_insights.get('visualization_data', {})
                },
                'diaper': {
                    'distribution': diaper_insights.get('type_distribution', {}),
                    'visualization_data': diaper_insights.get('visualization_data', {})
                }
            }
        
        return Response(visualization_data)

from rest_framework import generics
from .models import Baby,Feeding,DiaperChange,Sleep,Reminder,GrowthMilestone, Milestone, PumpingSession, DoctorAppointment, Medication, Recipe, Ingredient
from .serializers import BabySerializer,BabyInsightSerializer ,FeedingSerializer,DiaperChangeSerializer,SleepSerializer,ReminderSerializer,GrowthMilestoneSerializer,PumpingSessionSerializer,DoctorAppointmentSerializer,MedicationSerializer,BabyStatsSerializer, MilestoneSerializer, RegisterSerializer, RecipeSerializer, IngredientSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.response import Response
from django.db.models import Avg
from datetime import timedelta, date
from rest_framework.views import APIView
from .ai_insights import AIInsights
from .base_views import BabyOwnedCreateView, BabyOwnedDetailView, UserOwnedCreateView, UserOwnedDetailView
import logging

logger = logging.getLogger(__name__)

class BabyListCreateView(UserOwnedCreateView):
    serializer_class = BabySerializer
    model = Baby


class BabyDetailView(UserOwnedDetailView):
    serializer_class = BabySerializer
    model = Baby


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

class FeedingListCreateView(BabyOwnedCreateView):
    serializer_class = FeedingSerializer
    model = Feeding

class FeedingDetailView(BabyOwnedDetailView):
    serializer_class = FeedingSerializer
    model = Feeding

class DiaperChangeListCreateView(BabyOwnedCreateView):
    serializer_class = DiaperChangeSerializer
    model = DiaperChange

class DiaperChangeDetailView(BabyOwnedDetailView):
    serializer_class = DiaperChangeSerializer
    model = DiaperChange

class SleepListCreateView(BabyOwnedCreateView):
    serializer_class = SleepSerializer
    model = Sleep

class SleepDetailView(BabyOwnedDetailView):
    serializer_class = SleepSerializer
    model = Sleep

class ReminderListCreateView(UserOwnedCreateView):
    serializer_class = ReminderSerializer
    model = Reminder
    
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(user=self.request.user, baby=baby)
            except Baby.DoesNotExist:
                from rest_framework.exceptions import ValidationError
                raise ValidationError("You don't have permission to add data for this baby.")
        else:
            serializer.save(user=self.request.user)

class ReminderDetailView(UserOwnedDetailView):
    serializer_class = ReminderSerializer
    model = Reminder

class GrowthMilestoneListCreateView(BabyOwnedCreateView):
    serializer_class = GrowthMilestoneSerializer
    model = GrowthMilestone

class GrowthMilestoneDetailView(BabyOwnedDetailView):
    serializer_class = GrowthMilestoneSerializer
    model = GrowthMilestone


class BabyStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BabyStatsSerializer
    
    def get(self, request, baby_id):
        try:
            baby = Baby.objects.get(id=baby_id, user=request.user)
            logger.info(f"Retrieved stats for baby {baby_id} by user {request.user.id}")
        except Baby.DoesNotExist:
            logger.warning(f"Baby {baby_id} not found for user {request.user.id}")
            return Response({"error": "Baby not found"}, status=404)
        except Exception as e:
            logger.error(f"Error retrieving baby {baby_id} for user {request.user.id}: {str(e)}")
            return Response({"error": "Internal server error"}, status=500)

        try:
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
        except Exception as e:
            logger.error(f"Error calculating stats for baby {baby_id}: {str(e)}")
            return Response({"error": "Error calculating statistics"}, status=500)


class PumpingSessionListCreateView(UserOwnedCreateView):
    serializer_class = PumpingSessionSerializer
    model = PumpingSession

class PumpingSessionDetailView(UserOwnedDetailView):
    serializer_class = PumpingSessionSerializer
    model = PumpingSession

class DoctorAppointmentListCreateView(BabyOwnedCreateView):
    serializer_class = DoctorAppointmentSerializer
    model = DoctorAppointment

class DoctorAppointmentDetailView(BabyOwnedDetailView):
    serializer_class = DoctorAppointmentSerializer
    model = DoctorAppointment

class MedicationListCreateView(UserOwnedCreateView):
    serializer_class = MedicationSerializer
    model = Medication

class MedicationDetailView(UserOwnedDetailView):
    serializer_class = MedicationSerializer
    model = Medication

class MilestoneListCreateView(BabyOwnedCreateView):
    serializer_class = MilestoneSerializer
    model = Milestone

class MilestoneDetailView(BabyOwnedDetailView):
    serializer_class = MilestoneSerializer
    model = Milestone

class BabyAIInsightsView(APIView):
    serializer_class = BabyInsightSerializer
    permission_classes = [permissions.IsAuthenticated]

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
        # For now, treat POST the same as GET for generating reports
        return self.get(request, baby_id)

class RecipeListCreateView(UserOwnedCreateView):
    serializer_class = RecipeSerializer
    model = Recipe

class RecipeDetailView(UserOwnedDetailView):
    serializer_class = RecipeSerializer
    model = Recipe

class IngredientListCreateView(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Ingredient.objects.filter(recipe__user=self.request.user)

class IngredientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Ingredient.objects.filter(recipe__user=self.request.user)
            
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
    serializer_class = BabyInsightSerializer
    permission_classes = [permissions.IsAuthenticated]
    
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

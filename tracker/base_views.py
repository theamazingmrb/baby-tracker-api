from rest_framework import generics, permissions
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator


class BabyOwnedCreateView(generics.ListCreateAPIView):
    """Base view for models that belong to a baby owned by the user"""
    permission_classes = [permissions.IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='100/h', method='GET'))
    @method_decorator(ratelimit(key='user', rate='1000/h', method='POST'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(baby__user=self.request.user)
    
    def perform_create(self, serializer):
        # Verify the baby belongs to the current user
        baby_id = self.request.data.get('baby')
        if baby_id:
            from .models import Baby
            try:
                baby = Baby.objects.get(id=baby_id, user=self.request.user)
                serializer.save(baby=baby)
            except Baby.DoesNotExist:
                from rest_framework.exceptions import ValidationError
                raise ValidationError("You don't have permission to add data for this baby.")
        else:
            serializer.save()


class BabyOwnedDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Base detail view for models that belong to a baby owned by the user"""
    permission_classes = [permissions.IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='200/h', method='GET'))
    @method_decorator(ratelimit(key='user', rate='500/h', method='PUT'))
    @method_decorator(ratelimit(key='user', rate='100/h', method='DELETE'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(baby__user=self.request.user)


class UserOwnedCreateView(generics.ListCreateAPIView):
    """Base view for models that belong directly to the user"""
    permission_classes = [permissions.IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='100/h', method='GET'))
    @method_decorator(ratelimit(key='user', rate='1000/h', method='POST'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserOwnedDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Base detail view for models that belong directly to the user"""
    permission_classes = [permissions.IsAuthenticated]
    
    @method_decorator(ratelimit(key='user', rate='200/h', method='GET'))
    @method_decorator(ratelimit(key='user', rate='500/h', method='PUT'))
    @method_decorator(ratelimit(key='user', rate='100/h', method='DELETE'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

from rest_framework import permissions

class IsTenantUser(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own data.
    This permission works with models that have either:
    1. A direct user field (user=request.user)
    2. A relationship to Baby which has a user field (baby__user=request.user)
    """
    
    def has_permission(self, request, view):
        # Allow authenticated users to list and create
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Check if the object has a direct user field
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # Check if the object has a baby field that links to a user
        if hasattr(obj, 'baby') and hasattr(obj.baby, 'user'):
            return obj.baby.user == request.user
            
        # If we can't determine ownership, deny access
        return False

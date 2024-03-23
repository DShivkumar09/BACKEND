from rest_framework import permissions
from .models import User

class IsAdminUserOrCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return bool(request.method in permissions.SAFE_METHODS and request.user and request.user.is_authenticated and request.user.role == "admin")
        
        
    
    
class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user == obj)
    

        
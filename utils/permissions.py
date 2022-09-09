from rest_framework import permissions

# file contains all the custom permissions required for the project

class IsOwnerUserOrReadOnly(permissions.BasePermission):
    """Custom permissions."""
    def has_object_permission(self, request, view, instance):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.id == instance.id
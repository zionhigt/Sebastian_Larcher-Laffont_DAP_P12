from rest_framework.permissions import BasePermission, SAFE_METHODS
from authentication.models import Role


class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in SAFE_METHODS:
            if obj.salesman_id.id == request.user.id or request.user.role.id == Role.get_manager_role_id():
                return True
            return False
        else:
            return True

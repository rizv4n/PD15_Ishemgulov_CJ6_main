from rest_framework.permissions import BasePermission

from user.models import UserRoles


class ChangePermission(BasePermission):
    message = "Changing for non Admin user not allowed"

    def has_object_permission(self, request, view, obj):
        if obj.author.username == str(request.user) or request.user.role == UserRoles.ADMIN:
            return True
        else:
            return False


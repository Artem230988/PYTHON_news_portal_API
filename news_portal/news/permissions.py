from rest_framework.permissions import BasePermission


class IsNotBanned(BasePermission):
    """Не забанен"""
    def has_permission(self, request, view):
        return bool(request.user and (not request.user.is_banned))

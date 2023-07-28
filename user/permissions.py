from rest_framework.permissions import BasePermission


class IsUserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.username == obj.username

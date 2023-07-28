from rest_framework.permissions import BasePermission

class OwnerPermission(BasePermission):
    def has_permission(self, request, view):
        print(request.user.roles)
        if request.user.roles!='u':
            return True
        return False
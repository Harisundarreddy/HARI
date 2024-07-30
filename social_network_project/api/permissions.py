from rest_framework.permissions import BasePermission

class IsAuthenticatedOrCreate(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and view.basename == 'signup':
            return True
        return request.user and request.user.is_authenticated

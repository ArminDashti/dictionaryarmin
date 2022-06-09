from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: #Request methods is GET, HEAD, ... (NOT POST)
            return True
        return "armin" == str(request.user) #Allow to POST if username is armin. 
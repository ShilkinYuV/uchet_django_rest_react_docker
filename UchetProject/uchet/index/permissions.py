from rest_framework import permissions


class UchetPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)

        # Write permissions are only allowed to the owner of the snippet.
        return bool(request.user and request.user.is_staff)
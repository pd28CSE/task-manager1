from rest_framework import permissions

class TaskUpdatePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        taskId = request.path.split('/')[-2]
        is_authorized = bool(request.user and request.user.is_authenticated)
        if is_authorized:
            return request.user.usertask.filter(pk=taskId).exists()
        return False

    
    
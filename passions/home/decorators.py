from django.core.exceptions import PermissionDenied


def admin_required(function):
    def wrap(request, args=None, **kwargs):
        if request.user.admin == True:
            return function(request, **kwargs)
        else:
            raise PermissionDenied
    return wrap
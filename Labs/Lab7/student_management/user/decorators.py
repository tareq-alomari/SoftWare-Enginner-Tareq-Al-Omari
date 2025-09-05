from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    """
    Decorator to redirect logged-in users from pages like login/register.
    """
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('student:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    """
    Decorator to restrict access to views based on user groups.
    """
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('أنت غير مصرح لك بعرض هذه الصفحة')
        return wrapper_func
    return decorator

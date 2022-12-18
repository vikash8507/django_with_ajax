import functools
from django.shortcuts import redirect
from django.contrib import messages

def authentication_not_required(view_func, redirect_url="load_states"):

    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request,*args, **kwargs)
        messages.info(request, "You need to be logged out")
        return redirect(redirect_url)
    
    print('---Decorator Called---')
    return wrapper
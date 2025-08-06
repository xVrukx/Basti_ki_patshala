from django.shortcuts import render,redirect
from login.models import *

def homepage(request):
    user_id = request.session.get('user')

    if not user_id:
        return redirect('login:login')  # Redirect back if no session

    user_data = application.objects.get(id=user_id)

    return render(request, 'homepage.html', {'user': user_data})
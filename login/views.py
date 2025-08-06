from django.shortcuts import render, redirect
from login.models import application  # Explicit import
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['Password']
        phonenumber = request.POST['phonenumber']

        # ✅ Check if email already exists
        if application.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, 'application.html')

        # ✅ Create user (password hashing handled by model)
        user = application.objects.create(
            Username=Username,
            email=email,
            password=password,  # Let model hash this automatically
            phonenumber=phonenumber
        )

        # ✅ Set session and redirect
        request.session['user'] = user.id
        return redirect('homepage:homepage')

    return render(request, 'application.html')

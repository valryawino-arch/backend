
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('home')

        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('home')

        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('home')

        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'User registered successfully.')
            return redirect('home')
    return render(request,'home.html')

 
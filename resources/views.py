from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to your home page or any desired page after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            from django.contrib.auth import login
            login(request, form.get_user())
            # Redirect to a success page or home
            return redirect('/studyres/')  # Update with your desired URL name
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def index(request):
    return HttpResponse("Hello world")
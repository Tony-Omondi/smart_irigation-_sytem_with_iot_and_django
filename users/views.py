from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView



# Create your views here.
def index(request):
    return render(request, 'users/index.html', {})


# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
import pyrebase
from .forms import LoginForm, SignupForm
from django.conf import settings

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
auth = firebase.auth()

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                request.session['uid'] = user['idToken']  # Store the session token
                messages.success(request, "Logged in successfully!")
                return redirect('index')  # Redirect to a dashboard or home
            except:
                messages.error(request, "Failed to log in.")
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user = auth.create_user_with_email_and_password(email, password)
                messages.success(request, "Signed up successfully!")
                return redirect('login')  # Redirect to login after signup
            except Exception as e:
                messages.error(request, f"Failed to sign up: {e}")
                return redirect('signup')
    else:
        form = SignupForm()

    return render(request, 'users/signup.html', {'form': form})

def logout_view(request):
    try:
        del request.session['uid']  # Clear the session
    except KeyError:
        pass
    messages.success(request, "Logged out successfully!")
    return redirect('login')
# views.py

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'home.html')

@login_required
def market(request):
    return render(request, 'market.html')

def loginview(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)

        try:
            user = authenticate(username=username, password=password)
            print(user)
            if not user:
                raise User.DoesNotExist('Invalid username or password')
            login(request, user)
            return redirect('/dashboard')
        except User.DoesNotExist:
            return render(request, 'login.html', context={'error': 'Invalid username or password',})
        except Exception as e:
            return render(request, 'login.html', context={'error': str(e),})

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            return render(request, 'register.html', context={'error': 'Password does not match',})

        try:
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            login(request, new_user)
            return redirect('/dashboard')
        except Exception as e:
            if 'UNIQUE constraint' in str(e):
                if 'email' in str(e):
                    return render(request, 'register.html', context={'error': 'Email already exists',})
                return render(request, 'register.html', context={'error': 'Username already exists',})
            
            return render(request, 'register.html', context={'error': str(e),})

    return render(request, 'register.html')

def logoutview(request):
    logout(request)
    return redirect('/login/')
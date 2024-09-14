from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# View for the home page (public view)
def index(request):
    # Render the home page template 'home.html'
    return render(request, 'home.html')


# View for the market page (protected by login)
@login_required  # Ensures the user must be logged in to access the market page
def market(request):
    # Render the market page template 'market.html'
    return render(request, 'market.html')


# View for handling user login
def loginview(request):

    if request.method == "POST":
        # Get the username and password from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username, password)  # Print the entered credentials for debugging

        try:
            # Authenticate the user using Django's authentication system
            user = authenticate(username=username, password=password)
            print(user)  # Print the user object if authentication is successful
            
            # If user is not authenticated, raise an error
            if not user:
                raise User.DoesNotExist('Invalid username or password')
            
            # Log the user in and redirect to the dashboard
            login(request, user)
            return redirect('/dashboard')
        
        # Handle case where user credentials are invalid
        except User.DoesNotExist:
            return render(request, 'login.html', context={'error': 'Invalid username or password',})
        
        # Handle any other exceptions that may occur
        except Exception as e:
            return render(request, 'login.html', context={'error': str(e),})

    # Render the login page if the request method is not POST
    return render(request, 'login.html')


# View for handling user registration
def register(request):
    if request.method == "POST":
        # Get the registration details from the POST request
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        confirm_password = request.POST.get('password2')

        # Check if the passwords match, if not return an error message
        if password != confirm_password:
            return render(request, 'register.html', context={'error': 'Password does not match',})

        try:
            # Create a new user with the provided username and email
            new_user = User(username=username, email=email)
            # Set the user's password
            new_user.set_password(password)
            # Save the user to the database
            new_user.save()
            # Log the user in after successful registration and redirect to the dashboard
            login(request, new_user)
            return redirect('/dashboard')

        # Handle exceptions that may occur during user creation
        except Exception as e:
            # Handle case where the username or email already exists (UNIQUE constraint error)
            if 'UNIQUE constraint' in str(e):
                if 'email' in str(e):
                    return render(request, 'register.html', context={'error': 'Email already exists',})
                return render(request, 'register.html', context={'error': 'Username already exists',})
            
            # Render any other error messages
            return render(request, 'register.html', context={'error': str(e),})

    # Render the registration page if the request method is not POST
    return render(request, 'register.html')


# View for handling user logout
def logoutview(request):
    # Log the user out using Django's logout function
    logout(request)
    # Redirect the user to the login page after logout
    return redirect('/login/')

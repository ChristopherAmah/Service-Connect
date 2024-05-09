from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.core.mail import EmailMessage
from serviceconnectapp.forms import SignupForm
from dashboard.forms import ProfileUpdateForm
from django.http import Http404
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

# password reset modules
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
# password reset modules



from serviceconnectapp.models import *
from dashboard.models import *

# Create your views here.
def index(request):
    #query the Database to pull objects out
    categories = Category.objects.all()[:8]
    specials = Service.objects.filter(special=True)
    slide1 = Showcase.objects.get(pk=1)
    slide2 = Showcase.objects.get(pk=2)
    slide3 = Showcase.objects.get(pk=4)

    context = {
        'categories':categories,
        'specials':specials,
        'slide1':slide1,
        'slide2':slide2,
        'slide3':slide3,
    }
    
    return render(request, 'index.html', context)

def categories(request):
    categories = Category.objects.all()
    specials = Service.objects.filter(special=True)

    context = {
        'categories':categories,
        'specials':specials,
    }
    return render(request, 'categories.html', context)

def about_us(request):
    return render(request, 'aboutus.html')

@login_required(login_url='login')
def all_category(request):
    all_category = Service.objects.all()
    categories = Category.objects.all()

    context = {
        'all_category':all_category,
        'categories':categories,
    }
    return render(request, 'all_category.html', context)

@login_required(login_url='login')
def single_category(request, id):
    categories = Category.objects.all()
    single_category = Service.objects.filter(category_id = id)
    cat_title = Category.objects.get(pk=id)

    context = {
        'categories':categories,
        'category': single_category,
        'cat_title': cat_title,
    }
    return render(request, 'category.html', context)

# @login_required(login_url='login')
# def detail(request, id):
#     categories = Category.objects.all()
#     detail = Service.objects.get(pk=id)
#     review = Review.objects.all()

#     context = {
#         'categories':categories,
#         'detail':detail,
#         'review':review,
#     }
#     return render(request, 'detail.html', context)

@login_required(login_url='login')
def detail(request, id):
    try:
        categories = Category.objects.all()
        detail = Service.objects.get(pk=id)
        reviews = Review.objects.filter(service=detail)

        if request.method == 'POST':
            review_text = request.POST.get('review')
            if review_text:
                review = Review.objects.create(user=request.user, service=detail, comment=review_text)
                review.save()
                return redirect('detail', id=id)  # Redirect to the same page after submission

    except Service.DoesNotExist:
        raise Http404("Service does not exist")

    context = {
        'categories': categories,
        'detail': detail,
        'reviews': reviews,
    }
    return render(request, 'detail.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')



# def signup(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]

#         if password1 == password2:
#             try:
#                 user = User.objects.create_user(username, email, password1)
#                 user.save()
#                 auth.login(request, user)
#                 return redirect('index')
#             except:
#                 error_message = 'Error creating account'
#                 return render(request, 'signup.html', {'error_message': error_message})
#         else:
#             error_message = 'Password do not match'
#             return render(request, 'signup.html', {'error_message': error_message})
#     return render(request, 'signup.html')

def onboarding(request):
    if request.method == "POST":
        # Process the form data here and save it to the database
        # You can access form data using request.POST.get('<field_name>')
        # For example:
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                # newuser = Service(user = user)
                # newuser.first_name = user.first_name
                # newuser.last_name = user.last_name
                # newuser.email = user.email
                # newuser.save()
                # service = Service.objects.create(user=user)
                # service.save()

                auth.login(request, user)
                return redirect('index')
            except Exception as e:
                error_message = f'Error creating account: {str(e)}'
                print(e)  # Print the exception message to the console
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = 'Password do not match'
            return render(request, 'signup.html', {'error_message': error_message})

    # If the request method is GET, render the onboarding page template
    return render(request, 'onboarding.html')


# def signup(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]

#         if password1 == password2:
#             try:
#                 # Check if username or email already exist
#                 if User.objects.filter(username=username).exists():
#                     error_message = 'Username already exists'
#                 elif User.objects.filter(email=email).exists():
#                     error_message = 'Email already exists'
#                 else:
#                     # Create user if username and email are unique
#                     user = User.objects.create_user(username, email, password1)
#                     user.save()
#                     newuser = Profile(user = user)
#                     newuser.first_name = user.first_name
#                     newuser.last_name = user.last_name
#                     newuser.email = user.email
#                     newuser.save()
#                     auth.login(request, user)
#                     return redirect('index')
#                 return render(request, 'signup.html', {'error_message': error_message})
#             except Exception as e:
#                 # Handle other exceptions
#                 error_message = 'Error creating account: ' + str(e)
#                 return render(request, 'signup.html', {'error_message': error_message})
#         else:
#             error_message = 'Passwords do not match'
#             return render(request, 'signup.html', {'error_message': error_message})
#     return render(request, 'signup.html')

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Perform password validation
        try:
            validate_password(password1)
        except ValidationError as e:
            error_message = ', '.join(e.messages)
            return render(request, 'signup.html', {'error_message': error_message})

        if password1 == password2:
            try:
                # Check if username or email already exist
                if User.objects.filter(username=username).exists():
                    error_message = 'Username already exists'
                elif User.objects.filter(email=email).exists():
                    error_message = 'Email already exists'
                else:
                    # Create user if username and email are unique
                    user = User.objects.create_user(username, email, password1)
                    user.save()
                    newuser = Profile(user=user)
                    newuser.first_name = user.first_name
                    newuser.last_name = user.last_name
                    newuser.email = user.email
                    newuser.save()
                    auth.login(request, user)
                    return redirect('index')
                return render(request, 'signup.html', {'error_message': error_message})
            except Exception as e:
                # Handle other exceptions
                error_message = 'Error creating account: ' + str(e)
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match'
            return render(request, 'signup.html', {'error_message': error_message})
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
# dashboard configuration
def profile(request):
    profile_data = Profile.objects.get(user__username = request.user.username)

    context = {
        'profile_data':profile_data
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def profileupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = ProfileUpdateForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('profileupdate')
    context = {
        'form':form,
        'profile_data':profile_data,
    }
    return render(request, 'profileupdate.html', context)


@login_required(login_url='login')
def passwordupdate(request):
    profile_data = Profile.objects.get(user__username = request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password update successful')
            return redirect('profile')
        else:
            messages.error(request, form.errors)
            return redirect('passwordupdate')

    context = {
        'profile_data':profile_data,
        'form':form,
    }

    return render(request, 'profilepassword.html', context)
# dashboard configuration done

# def details(request, service_id):
    service = Service.objects.get(pk=service_id)
    # reviews = Review.objects.all()[:4]
    reviews = Review.objects.filter(service=service).order_by('-created_at')[:4]  # Get the latest 4 reviews
    
    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        user = request.user  # Assuming you're using Django's built-in authentication system
        Review.objects.create(service=service, user=user, review_text=review_text)
        return redirect('details', service_id=service_id)
    
    return render(request, 'details.html', {'service': service, 'reviews': reviews})


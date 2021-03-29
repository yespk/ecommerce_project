import re

from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import UserRegistrationForm, UserLoginForm
from login.models import User


# Create your views here.
def login(request):
    error_message = ''
    if request.method == 'POST':
        check_if_user_exists = User.objects.filter(email=request.POST.get('email', False),
                                                   password=request.POST.get('password', False)).exists()
        print("check: ", check_if_user_exists)
        if check_if_user_exists is True:
            user = User.objects.get(email=request.POST.get('email', False))
            print(user)
            if user is not None:
                return render(request, 'store/index.html')
        elif check_if_user_exists is False:
            print('Please try Again!!!')
            error_message = 'you are not registered!!!'
    context = {
        'UserForm': UserRegistrationForm,
        'UserLoginForm': UserLoginForm,
        'login_error_message': error_message,
    }
    return render(request, 'login/login.html', context)


def register(request):
    register_error_message = ''
    error_message_type = ''
    email_validate_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        print(User.objects.filter(email=email).exists())
        if first_name != '' and last_name != '' and email != '' and mobile != '':
            if re.search(email_validate_regex, email):
                if User.objects.filter(email=email).exists() is False:
                    if request.POST['password'] != request.POST['rpassword']:
                        error_message_type = 'danger'
                        register_error_message = 'password not matched!!!'
                    else:
                        error_message_type = 'success'
                        register_error_message = 'You are registered successfully!!!'
                else:
                    error_message_type = 'danger'
                    register_error_message = 'This email id is already registered!!!'
            else:
                error_message_type = 'danger'
                register_error_message = 'Please enter valid Email!!!'
        else:
            error_message_type = 'danger'
            register_error_message = 'Please fill all fields!!!'
    context = {
        'UserForm': UserRegistrationForm,
        'UserLoginForm': UserLoginForm,
        'register_error_message': register_error_message,
        'error_message_type': error_message_type,
    }
    return render(request, 'login/login.html', context)


def test1(request):
    context = {'UserForm': UserRegistrationForm, 'UserLoginForm': UserLoginForm, }
    return render(request, 'login/test.html', context)


def test(request, error_message):
    context = {
        'UserForm': UserRegistrationForm,
        'UserLoginForm': UserLoginForm,
        'error_message': 'password not matched!!!'
    }
    return render(request, 'login/test.html', context)

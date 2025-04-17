from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .forms import AuthenticateForm, UserCreateForm
from django.db import IntegrityError
import re

# Create your views here.

def logoutaccount(request):
    logout(request)
    return redirect('home')
    
def loginaccount(request):
    if request.method == "GET":
        return render(request, 'loginaccount.html', {'form': AuthenticateForm()})
    else:
        form = AuthenticateForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'loginaccount.html', {'form': form})
        
def signupaccount(request):
    if request.method == "GET":
        return render(request, 'signupaccount.html', {'form': UserCreateForm()})
    else:
        user_name = request.POST['username']
        pass_word = request.POST['password1']
        if re.search(r'@.*\.', user_name):
            if len(pass_word) >= 6:
                if re.search(r'(?=.*\d)(?=.*[A-Z])(?=.*[a-z])', pass_word):
                    if pass_word == request.POST['password2']:
                        try:
                            user = User.objects.create_user(username=user_name, password=pass_word, first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=user_name)
                            registrant = Group.objects.get(name='Registrant')
                            user.groups.add(registrant)
                            user.save()
                            login(request, user)
                            return redirect('loginaccount')
                        except IntegrityError:
                            return render(request, 'signupaccount.html', {'form': UserCreateForm(), "error": "Username Already Taken."})
                    else:
                        return render(request, 'signupaccount.html', {'form': UserCreateForm(), "error": "Passwords Do Not Match."})
                else:
                    return render(request, 'signupaccount.html', {"form": UserCreateForm(), "error": "Password must contain a number, a lowercase letter, and an uppercase letter."})
            else:
                return render(request, 'signupaccount.html', {"form": UserCreateForm(), "error": "Password must be at least 6 characters long."})
        else:
            return render(request, 'signupaccount.html', {"form": UserCreateForm(), "error": "Username must be an email."})

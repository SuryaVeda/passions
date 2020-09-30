from django.shortcuts import render, redirect, get_object_or_404
from .forms import VisitorRegisterForm, ProfileForm
from .models import Profile,User
from datetime import date, timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from urllib.parse import parse_qs
import json
from django.contrib import messages
# Create your views here.
def signin(request):
    template_name = 'registration/login.html'

    return render(request, template_name)
def signout(request):
    user = request.user
    logout(request)
    return redirect('home:home')

def visitor(request):
    template_name = 'accounts/signup.html'
    form = VisitorRegisterForm()
    if request.method == 'POST' :
        form = VisitorRegisterForm(request.POST)
        if form.is_valid():
            if form.clean_email():
                messages.error( request, "Email is taken!!, Try a new one or signin via google")
                return redirect('accounts:visitor')
            elif form.clean_password2():
                messages.error( request, "Passwords dont match")
                return redirect('accounts:visitor')
            else:
                user = form.save()
                #username=form.cleaned_data.get('username')
                #messages.success(request, f'Account created for {username}!')
                return redirect("/accounts/login")
    else:
        form = VisitorRegisterForm()
        return render(request, template_name, {'form':form})
    return render(request, template_name, {'form':form})



def google_signin(request):
    template_name = 'registration/login.html'
    profile = request.GET.get('profile')
    j = json.loads(profile)
    email = j["zu"]
    username = j["Ad"]
    try:
        search = User.objects.get(email = email)
        if search:
            if search.is_active:
                login(request, search)
            return redirect('home:home')
    except:
        user = User.objects.create(email=email, username=username)
        user.is_active = True
        user.outsider = True
        user.save()
        login(request, user)
        return redirect('home:home')




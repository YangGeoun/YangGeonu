from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm,CustomUserChangeForm
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('todos:index')
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/login.html',context)

def signup(request):
    if request.method=='POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request,'accounts/signup.html',context)


def logout(request):
    if request.method=='POST':
        auth_logout(request)
    return redirect('accounts:login')
    
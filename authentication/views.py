from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm,RegistrationForm
from .models import userInfo
from django.shortcuts import redirect



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_ = userInfo(username=form.cleaned_data['username'],password=form.cleaned_data['password'],email_id=form.cleaned_data['email_id'])
            user_.save()
            messages.success(message="Registration Complete",request=request)
            return redirect('login')
    else :
        form = RegistrationForm()

    return render(request,'register.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            messages.success(message="Logged in",request=request)
            return redirect('playlist')
    else :
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    user_ = userInfo.objects.filter(is_login=True)
    if user_:
        user_[0].is_login = False
        user_[0].save()
    return redirect('login')
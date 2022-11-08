from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User

from .forms import SubashForm,EditUserProfileForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.core.exceptions import ValidationError

# Create your views here.
def home_page(request):
    return render(request,'service/homepage.html')


def sign_up(request):
    if request.method == 'POST':
        fm =SubashForm(request.POST)
        if fm.is_valid():
            email = fm.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise ValidationError("Email exists")
            
            
            fm.save()   
            fm = SubashForm()
    
    else:
        fm = SubashForm()
    return render(request,'service/signup.html',{'form':fm})
    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data= request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)

                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')

        else:
            fm = AuthenticationForm()
    else:
        return HttpResponseRedirect('/profile/')
    return render(request,'service/login.html',{'form':fm})

def aboutus(request):
    return render(request,'service/aboutus.html')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect("/profile/")
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request,'service/profile.html',{'name':request.user,'form':fm},)

    else:
        return HttpResponseRedirect('/login/')
    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')



def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,  data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/profile/')
                
        else:
            fm = PasswordChangeForm(user = request.user)
        return render(request,'service/changepass.html',{'form':fm})
    
    else:
        return HttpResponseRedirect('/login/')

def service_page(request):
    return render(request,'service/services.html')

def contact_page(request):
    return render(request,'service/contact.html')
from cProfile import label
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from django.core.validators import EmailValidator



from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     email = forms.EmailField(unique=True)
    

class SubashForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)',widget=forms.PasswordInput)
    email = forms.EmailField(required=True, max_length=150, help_text='Required.',
       error_messages={'invalid': 'This does not look like an email address.'})
    
    class Meta:
        model = User
        # fields = ['username','email','address','phone_number']
        fields = ['id','first_name','last_name','username','email']
        labels = {'email':'Email'}

class EditUserProfileForm(UserChangeForm, SubashForm):
    password = None
    password1 = None
    password2= None
    class Meta:
        model = User
        # fields = ['username','email','date_joined','last_login','address','phone_number']
        fields = ['first_name','last_name','email','date_joined','last_login']

        labels ={'email':'Email'}

        
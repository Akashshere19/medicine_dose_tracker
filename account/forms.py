from .models import *
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class UserRegisterationForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=20)
    lastname =  forms.CharField(max_length=20)
    password = forms.PasswordInput()
    
    class Meta:
        model = User
        fields = ('username','email','firstname','lastname','password1','password2')
    


# A form to let users update their username and email
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email']


# form to update the profile fields
class UpdateProfileForm(forms.ModelForm):    
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    
    age = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = UserProfile
        fields = ['avatar','age','sex','country']
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from .forms import UserRegisterationForm,UpdateProfileForm,UpdateUserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
# Create your views here.

class CustomRegisterView(SuccessMessageMixin,CreateView):
    template_name = 'pages/register.html'
    form_class = UserRegisterationForm
    success_url = reverse_lazy('accounts:login')    
    success_message = "Account created successfully"
    
    

class CustomLoginPage(LoginView):
    template_name = 'pages/login.html'
    success_url = reverse_lazy('home')      
    

class CustomLogout(TemplateView):
    template_name = 'pages/logout.html'
    success_url = reverse_lazy('accounts:login')    


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance= request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance= request.user.userprofile)      
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
        else:
            user_form = UpdateUserForm()
            profile_form = UpdateProfileForm()
            return('profile')
            
       
        return render(request,'pages/profile.html')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'pages/change_pass.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
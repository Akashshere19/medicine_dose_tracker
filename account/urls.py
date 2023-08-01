from django.urls import path
from .import views
from .views import CustomLoginPage,CustomRegisterView,CustomLogout,PasswordChangeView
from django.contrib.auth import views as auth_views

app_name ='accounts'

urlpatterns=[
    path('', CustomLoginPage.as_view(), name='login'),
    path('register/',CustomRegisterView.as_view(), name='register'),
    path('logout', CustomLogout.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),    
    path('profile',views.profile, name='profile'),
    
    # authentication url
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="acc_pages/password_reset_confirm_form.html"),\
         name='password_reset_confirm'),

    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name="acc_pages/password_reset_done.html"),\
         name='password_reset_done'),
    
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name="acc_pages/password_reset_complete.html"),\
         name='password_reset_complete'), 
    
    # allauth path
    
    

]
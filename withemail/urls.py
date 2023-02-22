from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', signup, name= 'register'),
    path('verify/<token>',verify, name='verify'),
    path('login/', loginpage , name = 'login'),
    path('logout/', logoutpage , name = 'logout'),
    path('home/', home , name = 'home'),
    path('oldpassword/', oldpassword , name = 'oldpassword'),
    path('detailchange/', detailchange , name = 'detailchange'),

    # url for change password with an email address
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),

]

from django.urls import path
from .views import LogInView, RegisterView, ProfileView

from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('login/', LogInView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    # URL for initiating the password reset process. Displays a form where users can enter their email address.
    # Uses 'users/password_reset.html' as the form template and 'users/password_reset_email.html' for the email content.
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html',
        html_email_template_name='users/password_reset_email.html'),name='password_reset'),

    # URL displayed after a successful password reset request submission. Informs users to check their email.
    # Template: 'users/password_reset_done.html'
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    # URL for resetting the password after verifying the user's unique token and ID. Users can set a new password here.
    # Template: 'users/password_reset_confirm.html'
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # URL displayed after successfully completing the password reset process. Confirms the password has been updated.
    # Template: 'users/password_reset_complete.html'
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', ProfileView.as_view(), name='profile'),
]



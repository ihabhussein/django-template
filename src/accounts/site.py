from django.urls import path
from django.contrib.auth.views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('password_change/', PasswordChangeView.as_view(), 'password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), 'password_change_done'),

    path('password_reset/', PasswordResetView.as_view(), 'password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), 'password_reset_done'),
    path('password_reset_confirm/', PasswordResetConfirmView.as_view(), 'password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), 'password_reset_complete'),
]

def get_urls():
    return urlpatterns, 'accounts', 'accounts'

urls = get_urls()

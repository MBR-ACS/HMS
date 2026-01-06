from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('log_in/', LoginView.as_view(), name = 'log-in'),
    path('log_out/', LogoutView.as_view(), name='log-out')
]
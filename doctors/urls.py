from django.urls import path
from doctors import views

urlpatterns = [
    path('artho/', views.arthopedic),
    path('cardio/', views.cardiology),
    path('derma/', views.dermatology),
]
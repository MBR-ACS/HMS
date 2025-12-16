from django.urls import path
from apps.doctors import views
from apps.doctors import views

urlpatterns = [
    path('list_doctors/', views.list_doctors, name='list-doctors')
]
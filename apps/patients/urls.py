from django.urls import path
from apps.patients import views

urlpatterns = [
    path('list_patients/', views.list_patients, name='list-patients')
]
from django.urls import path
from apps.departments import views

urlpatterns = [
    path('list_departments/', views.list_departments, name = 'list-departments')
]
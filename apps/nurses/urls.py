from django.urls import path
from apps.nurses import views

urlpatterns = [
    path('list_nurses/', views.list_nurses, name='list-nurses')
]
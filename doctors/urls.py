from django.urls import path
from doctors import views

urlpatterns = [
    path('artho/', views.arthopedic),
    path('cardio/', views.cardiology),
    path('derma/', views.dermatology),
    path('list/', views.list_doc, name='list-doctors'),
    path('create_doctor/', views.create_doctor, name='create-doctor')
]
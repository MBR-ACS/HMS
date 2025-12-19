from django.urls import path
from apps.departments import views

urlpatterns = [
    path('list_departments/', views.list_departments, name = 'list-departments'),
    path('create_department/', views.add_department, name='add-dept'),
    path('edit_department/<int:dept_id>', views.edit_department, name='edit-dept'),
    path('delete_department/<int:dept_id>', views.delete_department, name='delete-dept'),
]
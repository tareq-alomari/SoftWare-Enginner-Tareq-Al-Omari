# teachers/urls.py
from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.teachers_home, name='teachers_home'),
    path('all/', views.read_teachers, name='teachers'),
    path('one/<int:id>/', views.read_one_teacher, name='teacher_one'),
    path('create/', views.create_teacher, name='new_teacher'),
    path('update/<int:id>/', views.update_teacher, name='edit_teacher'),
    path('delete/<int:id>/', views.delete_teacher, name='delete_teacher'),
    path('queries/', views.get_teachers_queries, name='teachers_queries'),
]
# students/urls.py
from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.read, name='students'),
    path('one/<int:id>/', views.read_one, name='student_one'),
    path('create/', views.create, name='newStudent'),
    path('update/<int:id>/', views.update, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('queries/', views.get_students, name='queries'),
]
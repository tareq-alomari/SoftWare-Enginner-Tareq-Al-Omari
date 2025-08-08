from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_view, name='students'),
]

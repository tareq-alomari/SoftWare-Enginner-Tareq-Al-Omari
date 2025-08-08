# students/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # رابط الصفحة الرئيسية للتطبيق
    path('', views.index, name='index'),

    # روابط الصفحات الأخرى 
    path('home/', views.home, name='home'), 
    path('show/', views.list_students, name='show'), 
    path('edit/', views.edit_students, name='edit'), 
    path('delete/', views.delete_students, name='delete'), 
]
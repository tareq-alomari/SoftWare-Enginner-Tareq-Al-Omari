# courses/urls.py
from django.urls import path
from . import views

app_name = 'course'
urlpatterns = [
    path('', views.courses_home, name='courses_home'),
    path('all/', views.course_list, name='course_list'),
    path('detail/<int:id>/', views.course_detail, name='course_detail'),
    path('create/', views.course_create, name='course_create'),
    path('update/<int:id>/', views.course_update, name='course_update'),
    path('delete/<int:id>/', views.course_delete, name='course_delete'),
    path('queries/', views.course_queries, name='course_queries'),
]
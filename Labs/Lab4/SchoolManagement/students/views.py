from django.shortcuts import render
from .models import Students

def students_list(request):
    all_students = Students.objects.all()
    context = {'students': all_students}
    return render(request, 'students_list.html', context)
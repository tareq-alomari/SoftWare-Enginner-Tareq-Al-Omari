# students/views.py

from django.shortcuts import render

# دالة لعرض صفحة index.html
def index(request):
    name = {"fname": "Tareq"} 
    return render(request, 'index.html', name)

# دالة لعرض صفحة home.html
def home(request):
    return render(request, 'home.html')

# دالة لعرض بيانات الطلاب في showstudents.html
def list_students(request):
    students = {
        "name": "Tareq", 
        "marks": [90, 95, 98, 97], 
        "eachsub": {
            "Software Engineering": 96, 
            "Image Processing": 94, 
            "Client and Server Programming": 96 
        }
    }
    return render(request, 'showstudents.html', students) 

# دالة لعرض صفحة تعديل البيانات editstudents.html
def edit_students(request):
    students = {
        "total": 286, 
        "marks": {
            "Software Engineering": 96, 
            "Image Processing": 94, 
            "Client and Server Programming": 96 
        }
    }
    return render(request, 'editstudents.html', students) 

# دالة لعرض صفحة الحذف deletestudents.html          
def delete_students(request):
    return render(request, 'deletestudents.html') 
    
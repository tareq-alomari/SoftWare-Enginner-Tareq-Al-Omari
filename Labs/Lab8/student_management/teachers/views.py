# teachers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from django.db.models import Q

# الصفحة الرئيسية للمعلمين
def teachers_home(request):
    return render(request, 'teachers/teachers_home.html')

# عرض جميع المعلمين
def read_teachers(request):
    teachers = Teacher.objects.all()
    teachers_count = teachers.count()
    return render(request, 'teachers/all_teachers.html', {
        'teachers': teachers,
        'teachers_count': teachers_count
    })

# عرض معلم واحد
def read_one_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    return render(request, 'teachers/teacher_one.html', {'teacher': teacher})

# إنشاء معلم جديد
def create_teacher(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        specialty = request.POST.get('specialty')
        years_of_experience = request.POST.get('years_of_experience')
        salary = request.POST.get('salary')
        is_active = request.POST.get('is_active') == 'on'
        notes = request.POST.get('notes')
        
        new_teacher = Teacher(
            f_name=f_name, 
            l_name=l_name, 
            age=age, 
            specialty=specialty,
            years_of_experience=years_of_experience, 
            salary=salary, 
            is_active=is_active,
            notes=notes
        )
        new_teacher.save()
        return render(request, 'teachers/messages/created.html')
    else:
        return render(request, 'teachers/insert_teacher.html')

# تحديث بيانات المعلم
def update_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    
    if request.method == 'POST':
        teacher.f_name = request.POST.get('f_name')
        teacher.l_name = request.POST.get('l_name')
        teacher.age = request.POST.get('age')
        teacher.specialty = request.POST.get('specialty')
        teacher.years_of_experience = request.POST.get('years_of_experience')
        teacher.salary = request.POST.get('salary')
        teacher.is_active = request.POST.get('is_active') == 'on'
        teacher.notes = request.POST.get('notes')
        teacher.save()
        return render(request, 'teachers/messages/updated.html')
    else:
        return render(request, 'teachers/update_teacher.html', {'teacher': teacher})

# حذف معلم
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return render(request, 'teachers/messages/deleted.html')

# استعلامات متقدمة للمعلمين
def get_teachers_queries(request):
    # ترتيب حسب الراتب تصاعدياً
    teachers_asc = Teacher.objects.all().order_by("salary")
    
    # ترتيب حسب الراتب تنازلياً
    teachers_desc = Teacher.objects.all().order_by("-salary")
    
    # البحث عن أسماء تحتوي على حرف معين
    teachers_contains = Teacher.objects.filter(f_name__contains='ا')
    
    # البحث بسنوات خبرة محددة
    teachers_in = Teacher.objects.filter(years_of_experience__in=[5, 10, 15])
    
    # البحث ضمن نطاق محدد للراتب
    teachers_range = Teacher.objects.filter(salary__range=[3000, 5000])
    
    # البحث بقيمة محددة للتخصص
    teachers_exact = Teacher.objects.filter(specialty="رياضيات")
    
    # استبعاد معلم معين
    teachers_exclude = Teacher.objects.all().exclude(f_name="أحمد")
    
    # استعلام مركب
    teachers_complex = Teacher.objects.all().exclude(Q(f_name="أحمد") | Q(age=40))
    
    return render(request, 'teachers/teachers_queries.html', {
        'teachers_asc': teachers_asc,
        'teachers_desc': teachers_desc,
        'teachers_contains': teachers_contains,
        'teachers_in': teachers_in,
        'teachers_range': teachers_range,
        'teachers_exact': teachers_exact,
        'teachers_exclude': teachers_exclude,
        'teachers_complex': teachers_complex
    })
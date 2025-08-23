# courses/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Course
from .forms import CourseForm

# الصفحة الرئيسية للمواد الدراسية
def courses_home(request):
    return render(request, 'courses/courses_home.html')

# عرض جميع المواد الدراسية
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# عرض مادة دراسية واحدة
def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses/course_detail.html', {'course': course})

# إنشاء مادة دراسية جديدة
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة المادة الدراسية بنجاح')
            return redirect('course:course_list')
    else:
        form = CourseForm()
    
    return render(request, 'courses/course_form.html', {
        'form': form,
        'title': 'إضافة مادة دراسية جديدة'
    })

# تحديث مادة دراسية
def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث المادة الدراسية بنجاح')
            return redirect('course:course_list')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'courses/course_form.html', {
        'form': form,
        'title': 'تعديل المادة الدراسية',
        'course': course
    })

# حذف مادة دراسية
def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'تم حذف المادة الدراسية بنجاح')
        return redirect('course:course_list')
    
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

# استعلامات متقدمة
def course_queries(request):
    # مواد مفعلة فقط
    active_courses = Course.objects.filter(is_active=True)
    
    # مواد حسب المستوى
    level_courses = {}
    for level_code, level_name in Course.LEVEL_CHOICES:
        level_courses[level_name] = Course.objects.filter(level=level_code, is_active=True)
    
    # مواد ذات ساعات معتمدة أكثر من 3
    high_credit_courses = Course.objects.filter(credit_hours__gt=3)
    
    return render(request, 'courses/course_queries.html', {
        'active_courses': active_courses,
        'level_courses': level_courses,
        'high_credit_courses': high_credit_courses,
    })
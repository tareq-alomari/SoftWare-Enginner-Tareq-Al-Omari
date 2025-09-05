# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student  # استيراد Student فقط من students.models
from teachers.models import Teacher  # استيراد Teacher من teachers.models
from courses.models import Course  # استيراد Teacher من teachers.models
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url='user:login') # HW - Authorization
# الصفحة الرئيسية
def home(request):
    students_count = Student.objects.count()
    teachers_count = Teacher.objects.count()
    courses_count = Course.objects.count()  # تأكد من استيراد النموذج
    
    return render(request, 'home.html', {
        'students_count': students_count,
        'teachers_count': teachers_count,
        'courses_count': courses_count
    })
    
@login_required(login_url='user:login')
# عرض جميع الطلاب
def read(request):
    status = request.GET.get('q')  # الحصول على قيمة الفلتر من الرابط

    if status == 'all' or status is None:
        # إذا كانت القيمة "all" أو لا يوجد فلتر، اعرض جميع الطلاب
        students = Student.objects.all()
    else:
        # قم بتحويل القيمة إلى Boolean (True/False) للفلترة
        status_bool = status.lower() == 'true'
        students = Student.objects.filter(status=status_bool)
    
    students_count = students.count()
    
    return render(request, 'allStudents.html', {
        'students': students,
        'students_count': students_count
    })
    
@login_required(login_url='user:login')
# عرض طالب واحد
def read_one(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_one.html', {'student': student})


@login_required(login_url='user:login')
def create(request):
    if request.method == 'POST':
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        age = request.POST.get('age')
        gpa = request.POST.get('gpa')
        level = request.POST.get('level')
        status = request.POST.get('status') == 'on'
        report = request.POST.get('report')
        
        # === التعامل مع الملفات المرفوعة ===
        image = request.FILES.get('image')
        file_report = request.FILES.get('file_report')
        
        new_student = Student(
            f_name=f_name, 
            l_name=l_name, 
            age=age, 
            gpa=gpa,
            level=level, 
            status=status, 
            report=report,
            image=image,            # إضافة الصورة
            file_report=file_report # إضافة ملف التقرير
        )
        new_student.save()
        return render(request, 'messages/created.html')
    else:
        return render(request, 'insert_student.html')
    
@login_required(login_url='user:login')
# تحديث بيانات الطالب
def update(request, id):
    student = get_object_or_404(Student, id=id)
    
    if request.method == 'POST':
        student.f_name = request.POST.get('f_name')
        student.l_name = request.POST.get('l_name')
        student.age = request.POST.get('age')
        student.gpa = request.POST.get('gpa')
        student.level = request.POST.get('level')
        student.status = request.POST.get('status') == 'on'
        student.report = request.POST.get('report')

        #  تحديث الصورة إذا تم رفع صورة جديدة
        if 'image' in request.FILES:
            student.image = request.FILES['image']

        #  تحديث ملف التقرير إذا تم رفع ملف جديد
        if 'file_report' in request.FILES:
            student.file_report = request.FILES['file_report']

        student.save()
        return render(request, 'messages/updated.html')

    return render(request, 'update_student.html', {'student': student})

@login_required(login_url='user:login')
# # حذف طالب
def delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return render(request, 'messages/deleted.html')

@login_required(login_url='user:login')
# استعلامات متقدمة
def get_students(request):
    # ترتيب حسب المعدل تصاعدياً
    students_asc = Student.objects.all().order_by("gpa")
    
    # ترتيب حسب المعدل تنازلياً
    students_desc = Student.objects.all().order_by("-gpa")
    
    # البحث عن أسماء تحتوي على حرف معين
    students_contains = Student.objects.filter(f_name__contains='ا')
    
    # البحث بقيم محددة في المعدل
    students_in = Student.objects.filter(gpa__in=[90.00, 91.00])
    
    # البحث ضمن نطاق محدد
    students_range = Student.objects.filter(gpa__range=[89, 91])
    
    # البحث بقيمة محددة
    students_exact = Student.objects.filter(gpa=90.00)
    
    # استبعاد طالب معين
    students_exclude = Student.objects.all().exclude(f_name="طارق")
    
    # استعلام مركب
    students_complex = Student.objects.all().exclude(Q(f_name="طارق") | Q(age=22))
    
    return render(request, 'showstudents.html', {
        'students_asc': students_asc,
        'students_desc': students_desc,
        'students_contains': students_contains,
        'students_in': students_in,
        'students_range': students_range,
        'students_exact': students_exact,
        'students_exclude': students_exclude,
        'students_complex': students_complex
    })
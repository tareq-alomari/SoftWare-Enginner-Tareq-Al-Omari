# academics/models.py
from django.db import models
from students.models import Student # استيراد نموذج الطالب من تطبيقه
from teachers.models import Teacher # استيراد نموذج المعلم من تطبيقه

# === 1. علاقة واحد لواحد (One-to-One) ===
# كل مدير مدرسة له مكتب واحد فقط
class Office(models.Model):
    office_number = models.CharField(max_length=10, unique=True, verbose_name="رقم المكتب")
    building = models.CharField(max_length=50, verbose_name="المبنى")

    def __str__(self):
        return f"مكتب رقم {self.office_number} في مبنى {self.building}"

class Principal(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, verbose_name="المعلم (المدير)")
    office = models.OneToOneField(Office, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="المكتب")

    def __str__(self):
        return f"المدير: {self.teacher.f_name} {self.teacher.l_name}"

# ---

# === 2. علاقة كثير لواحد (Many-to-One / ForeignKey) ===
# كل قسم أكاديمي يضم عدة مواد دراسية
class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="عنوان المادة")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="القسم")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name="المعلم")

    def __str__(self):
        return self.title

# ---

# === 3. علاقة كثير لكثير (Many-to-Many) ===
# الطالب الواحد يمكنه التسجيل في عدة مواد، والمادة الواحدة بها عدة طلاب
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="المادة")
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="تاريخ التسجيل")

    class Meta:
        # يضمن عدم تسجيل الطالب في نفس المادة أكثر من مرة
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} مسجل في {self.course}"
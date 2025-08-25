# students/models.py
from django.db import models

class Student(models.Model):
    f_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    l_name = models.CharField(max_length=50, verbose_name="الاسم الأخير")
    age = models.IntegerField(verbose_name="العمر")
    level = models.CharField(max_length=10, verbose_name="المرحلة الجامعية")
    gpa = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="المعدل")
    status = models.BooleanField(default=True, verbose_name="منتظم")
    report = models.TextField(blank=True, null=True, verbose_name="ملاحظة")
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"
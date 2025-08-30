# teachers/models.py
from django.db import models

class Teacher(models.Model):
    f_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    l_name = models.CharField(max_length=50, verbose_name="الاسم الأخير")
    age = models.IntegerField(verbose_name="العمر")
    specialty = models.CharField(max_length=100, verbose_name="التخصص")
    years_of_experience = models.IntegerField(verbose_name="سنوات الخبرة")
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="الراتب")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    notes = models.TextField(blank=True, null=True, verbose_name="ملاحظات")
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
    class Meta:
        verbose_name = "معلم"
        verbose_name_plural = "المعلمين"
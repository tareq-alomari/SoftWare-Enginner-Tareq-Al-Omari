# courses/models.py
from django.db import models

class Course(models.Model):
    LEVEL_CHOICES = [
        ('1', 'الأولى'),
        ('2', 'الثانية'),
        ('3', 'الثالثة'),
        ('4', 'الرابعة'),
        ('5', 'الخامسة'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="اسم المادة")
    code = models.CharField(max_length=10, unique=True, verbose_name="كود المادة")
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES, verbose_name="المستوى")
    credit_hours = models.IntegerField(verbose_name="عدد الساعات المعتمدة")
    description = models.TextField(blank=True, null=True, verbose_name="وصف المادة")
    is_active = models.BooleanField(default=True, verbose_name="مفعلة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاريخ التحديث")
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    class Meta:
        verbose_name = "مادة دراسية"
        verbose_name_plural = "المواد الدراسية"
        ordering = ['level', 'name']
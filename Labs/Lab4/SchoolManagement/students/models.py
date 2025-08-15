from django.db import models

# Create your models here.
class Students(models.Model):
    LEVELS = [
        ('1','level One'),
        ('2','level Two'),
        ('3','level Three'),
        ('4','level Four'),

    ]
    f_name = models.CharField(max_length = 100 , default = "Student")
    l_name = models.CharField(max_length=100, default="Student") # Corrected from l_name
    age = models.IntegerField()
    level = models.CharField(max_length=20, choices=LEVELS)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    status = models.BooleanField(default=True) # Corrected from statust
    report = models.TextField(max_length=300, blank=True) # Corrected from reporet, added blank=True

    def __str__(self):
        return f"{self.f_name} {self.l_name}"
    
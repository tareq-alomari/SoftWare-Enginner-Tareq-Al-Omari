# academics/admin.py
from django.contrib import admin
from .models import Office, Principal, Department, Course, Enrollment

admin.site.register(Office)
admin.site.register(Principal)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Enrollment)
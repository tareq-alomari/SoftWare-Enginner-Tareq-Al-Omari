# courses/forms.py
from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'level', 'credit_hours', 'description', 'is_active']
        labels = {
            'name': 'اسم المادة',
            'code': 'كود المادة',
            'level': 'المستوى',
            'credit_hours': 'عدد الساعات المعتمدة',
            'description': 'وصف المادة',
            'is_active': 'مفعلة',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم المادة'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل كود المادة'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'credit_hours': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 6}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'أدخل وصف المادة'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
    
    def clean_code(self):
        code = self.cleaned_data.get('code')
        # التحقق من أن الكود فريد (مع استثناء الحالة الحالية في التحديث)
        if self.instance and self.instance.pk:
            if Course.objects.filter(code=code).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError('كود المادة موجود مسبقاً')
        else:
            if Course.objects.filter(code=code).exists():
                raise forms.ValidationError('كود المادة موجود مسبقاً')
        return code
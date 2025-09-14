from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    # نضيف حقل البريد الإلكتروني فقط، لأن حقول كلمة المرور موجودة مسبقًا
    email = forms.EmailField(
        label="البريد الإلكتروني",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # نحدد الحقول بالترتيب الذي نريده أن يظهر في الفورم
        fields = ('username', 'email', 'password', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # تعديل خصائص الحقول الموروثة
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المستخدم'})
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'كلمة المرور'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تأكيد كلمة المرور'})
        
        # تعديل التسميات (Labels) لتكون باللغة العربية
        self.fields['username'].label = "اسم المستخدم"
        self.fields['password'].label = "كلمة المرور"
        self.fields['password2'].label = "تأكيد كلمة المرور"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("هذا البريد الإلكتروني مستخدم من قبل.")
        return email
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .decorators import unauthenticated_user, allowed_users
from emails.views import send_welcome_email # **استيراد دالة الإيميل**

@unauthenticated_user
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # **إرسال الإيميل الترحيبي بعد حفظ المستخدم مباشرة**
            send_welcome_email(user.username, user.email)
            login(request, user)
            messages.success(request, f"تم تسجيلك بنجاح، مرحباً بك {user.username}!")
            return redirect('student:home')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})

@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student:home')
            else:
                messages.error(request, "اسم المستخدم أو كلمة المرور غير صالحة.")
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

@login_required(login_url='user:login')
def logout_user(request):
    logout(request)
    return redirect('user:login')

@login_required(login_url='user:login')
@allowed_users(allowed_roles=['admin'])
def admin_page(request):
    return render(request, 'user/admin_page.html')

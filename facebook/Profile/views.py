from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # pass return HttpResponse("صفحة الملف الشخصي (Profile)")
    return render(request, 'Profile/home.html')

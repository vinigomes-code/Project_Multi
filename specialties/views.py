from django.shortcuts import render
#from django.http import HttpResponse

from .models import Specialties, Exam

#HTTP Request RETURN HTTP Response
def home(request):
    specialties =Specialties.objects.all()

    return render(request, 'pages/index.html', context={
        'specialties': specialties,
    })

def about(request):
    specialties = Specialties.objects.all()
    exams = Exam.objects.all()

    return render(request, 'pages/about.html', context={
        'specialties': specialties,
        'exams': exams,
    })


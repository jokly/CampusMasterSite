from django.shortcuts import render

# Create your views here.

def show_complaints(request):
    return render(request, 'campus_master/complaints.html', {})


def login(request):
    return render(request, 'campus_master/login.html', {})


def logout(request):
    return render(request, 'campus_master/logout.html', {})

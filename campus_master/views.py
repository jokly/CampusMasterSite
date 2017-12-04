from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Complaint

# Create your views here.

def main(request):
    return render(request, 'campus_master/index.html', {})

def complaints(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')

    data = Complaint.objects.all()

    return render(request, 'campus_master/complaints.html', {})

from django.shortcuts import render

# Create your views here.

def show_complaints(request):
    return render(request, 'campus_master/show_complaints.html', {})

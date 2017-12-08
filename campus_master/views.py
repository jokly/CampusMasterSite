from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import xlwt
from .models import Complaint, Status

# Create your views here.

def main(request):
    return render(request, 'campus_master/index.html', {})

@login_required
def complaints(request):
    data = Complaint.objects.all()

    return render(request, 'campus_master/complaints.html', {'data': data})

@login_required
def export_complaints_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="complaints.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Жалобы')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Комната', 'Жалоба']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    data = Complaint.objects.all()

    for row in data:
        row_num += 1

        ws.write(row_num, 0, row.chat.room, font_style)
        ws.write(row_num, 1, row.text, font_style)

    wb.save(response)

    return response


def status(request):
    data = Status.objects.all()

    return render(request, 'campus_master/status.html', {'data': data})

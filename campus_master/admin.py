from django.contrib import admin
from .models import User, Complaint, Status, News

# Register your models here.
admin.site.register(User)
admin.site.register(Complaint)
admin.site.register(Status)
admin.site.register(News)

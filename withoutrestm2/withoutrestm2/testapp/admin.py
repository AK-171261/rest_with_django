from django.contrib import admin
from testapp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rollno', 'marks', 'gf', 'bf']


# Register your models here.
admin.site.register(Student, StudentAdmin)

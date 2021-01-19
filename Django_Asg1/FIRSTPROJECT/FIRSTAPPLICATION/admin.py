from django.contrib import admin
from . models import student, college, marks

# Register your models here.

admin.site.register(student)
admin.site.register(college)
admin.site.register(marks)


from django.contrib import admin
from .models import Student, Course, ApplyCourse, Admin

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(ApplyCourse)
admin.site.register(Admin)
from django.contrib import admin

from .models import Companies, Employee, Class, Student


admin.site.register(Companies)
admin.site.register(Employee)
admin.site.register(Class)
admin.site.register(Student)

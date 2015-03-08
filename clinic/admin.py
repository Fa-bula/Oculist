from django.contrib import admin

# Register your models here.

from clinic.models import Doctor, Schedule

class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Личная информация', {'fields': ['lastName', 'firstName', 'patronymic', 'birthDate']}),
        ('Прочее', {'fields': ['education', 'schedule']}),
    ]

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Schedule)


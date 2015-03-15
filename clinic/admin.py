from django.contrib import admin
from clinic.models import Doctor, Schedule, Service, Comment, Patient, Visit
from django.contrib.auth.models import User

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Личная информация', {'fields': ['lastName', 'firstName', 'patronymic', 'birthDate']}),
        ('Прочее', {'fields': ['doctorType', 'education', 'schedule', 'photo']}),
    ]

class CommentAdmin(admin.ModelAdmin):
    fields = ['service', 'content']

class PatientInline(admin.StackedInline):
    model = Patient
    can_delete = False
    verbose_name_plural = 'Пациент'

# Define a new User admin
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'is_staff', 'is_active']
    inlines = (PatientInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Schedule)
admin.site.register(Visit)
admin.site.register(Service)
admin.site.register(Comment, CommentAdmin)

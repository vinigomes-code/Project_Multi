from django.contrib import admin

from .models import Specialties, Exam

class SpecialtiesAdmin(admin.ModelAdmin):
    ...

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    ...

admin.site.register(Specialties, SpecialtiesAdmin)


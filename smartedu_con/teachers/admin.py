from django.contrib import admin
from .models import Teacher, Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'job')

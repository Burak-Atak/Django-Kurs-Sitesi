from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)

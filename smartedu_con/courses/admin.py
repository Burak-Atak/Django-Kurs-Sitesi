from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'available', 'updated_at', 'created_at')
    list_filter = ('created_at', 'available')
    search_fields = ('name', 'description')

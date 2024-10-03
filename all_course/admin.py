from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'instractor', 'start_class', 'course_fee')
    list_filter = ('course_name', 'instractor', 'start_class')
    search_fields = ('course_name', 'course_code', 'description')
    ordering = ('start_class',)
    prepopulated_fields = {'course_code': ('course_name',)}  # Automatically populate course_code based on course_name
    fields = ('course_name', 'course_code', 'image', 'description', 'entry_course', 'instractor', 'blogs', 'module', 'course_time', 'course_length', 'total_sit', 'course_fee', 'start_class')
    # Optionally customize the admin form fields

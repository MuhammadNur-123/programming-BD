from django.contrib import admin
from .models import Enrolled

@admin.register(Enrolled)
class EnrolledAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'enroll_by', 'enroll_date', 'payment_method')
    search_fields = ('course_name__course_name', 'enroll_by__username')
    list_filter = ('payment_method',)

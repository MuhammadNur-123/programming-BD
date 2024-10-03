from django.contrib import admin
from .models import Blog, Course_Module

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_name', 'author')
    search_fields = ('blog_name', 'description')
    list_filter = ('author',)

@admin.register(Course_Module)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'modules')
    search_fields = ('modules',)
    list_filter = ('course_name',)

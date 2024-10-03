from django import forms
from .models import Blog, Course_Module

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_name', 'author', 'description']

class CourseModuleForm(forms.ModelForm):
    class Meta:
        model = Course_Module
        fields = ['course_name', 'modules']

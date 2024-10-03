from django.urls import path
from .views import (
    blog_list, blog_detail, blog_create, blog_update, blog_delete,
    course_module_list, course_module_detail, course_module_create,
    course_module_update, course_module_delete, download_pdf1
)

urlpatterns = [
    # Blog URLs
    path('blogs/', blog_list, name='blog_list'),
    path('blogs/<int:pk>/', blog_detail, name='blog_detail'),
    path('blogs/new/', blog_create, name='blog_create'),
    path('blogs/<int:pk>/edit/', blog_update, name='blog_update'),
    path('blogs/<int:pk>/delete/', blog_delete, name='blog_delete'),

    # Course Module URLs
    path('course-modules/', course_module_list, name='course_module_list'),
    path('course-modules/<int:pk>/', course_module_detail, name='course_module_detail'),
    path('course-modules/new/', course_module_create, name='course_module_create'),
    path('course-modules/<int:pk>/edit/', course_module_update, name='course_module_update'),
    path('course-modules/<int:pk>/delete/', course_module_delete, name='course_module_delete'),

    path('course-modules/<int:pk>/download/', download_pdf1, name='download_pdf1'),
]

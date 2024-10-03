from django.urls import path
from .views import course_list, course_detail, course_create, course_update, course_delete,course_box

urlpatterns = [
    path('list/', course_list, name='course_list'),
    path('box/', course_box, name='course_box'),
    path('course/<int:pk>/', course_detail, name='course_detail'),
    path('course/new/', course_create, name='course_create'),
    path('course/<int:pk>/edit/', course_update, name='course_update'),
    path('course/<int:pk>/delete/', course_delete, name='course_delete'),
]

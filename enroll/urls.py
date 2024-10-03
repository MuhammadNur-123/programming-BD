from django.urls import path
from . import views

urlpatterns = [
    path('enrolled/', views.enrolled_list, name='enrolled_list'),
    path('enrolled/new/', views.enrolled_create, name='enrolled_create'),
    path('enrolled/<int:pk>/edit/', views.enrolled_update, name='enrolled_update'),
    path('enrolled/<int:pk>/delete/', views.enrolled_delete, name='enrolled_delete'),
    path('enrolled/<int:pk>/', views.enrolled_detail, name='enrolled_detail'),
    path('support_course/', views.support_course, name='support_course'),
    path('enrolled/<int:pk>/download/', views.enrolled_download_pdf, name='enrolled_download_pdf'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('footer/', views.contact, name='contact'),
  
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('youtube/', views.youtube_search, name='youtube_search'),
    path('password-reset/', views.password_reset_request, name='password_reset_request'),
    path('password-reset-confirm/', views.password_reset_confirm, name='password_reset_confirm'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
]

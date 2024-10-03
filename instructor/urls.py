from django.urls import path
from .views import create_instractor, update_instractor, delete_instractor, instractor_list,instractor_profile

urlpatterns = [
    path('create/', create_instractor, name='create_instractor'),
    path('update/<int:id>/',update_instractor, name='update_instractor'),
    path('instractor/<int:id>/', delete_instractor, name='delete_instractor'),
    path('instractor/', instractor_list, name='instractor_list'),
    path('instractor_profile/',instractor_profile, name='instractor_profile'),
  
]

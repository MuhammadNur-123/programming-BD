from django.urls import path
from . import views

urlpatterns = [
   
    path('update_user/<int:pk>/', views.update_user, name='update_user'),
    path('delete_user/<int:pk>/', views.delete_user, name='delete_user'),
]



from django.urls import path,include
from .views import user_list,profile_view,update_user,update_user_status,delete_user,create_user

urlpatterns = [

    path('create_user/',create_user, name='create_user'),
    path('user_list/', user_list, name="user_list"),
    path('profile/', profile_view, name='profile_view'),
    path('update_user_status/<int:user_id>/',update_user_status, name='update_user_status'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'), 
    path('update_user/<int:user_id>/', update_user, name='update_user'),
]

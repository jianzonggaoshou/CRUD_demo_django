from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_manager_check, name='user_manager_check'),
    path('add/', views.user_manager_add, name='user_manager_add'),
    path('delete/', views.user_manager_delete, name="user_delete"),
    path('update/', views.user_manager_update, name="user_update")
]

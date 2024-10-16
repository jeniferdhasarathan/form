from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('user/new/', views.user_form, name='user_form'),
    path('user/<int:id>/edit/', views.user_form, name='user_update'),
    path('user/<int:id>/delete/', views.user_confirm_delete, name='user_delete'),
]

from django.urls import path
from. import views

urlpatterns = [
    path('', views.login, name='login'),
    path('sign-up/', views.register, name='sign-up'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('userlogout/', views.user_logout, name='userlogout'),
    path('dashboard/view/', views.view_data, name="view"),
    path('dashboard/add/', views.add_data, name="add"),
    path('dashboard/delete/', views.delete_data, name="delete"),
    path('dashboard/modify/', views.modify_data, name="modify"),
    path('dashboard/help/', views.ai_assistant, name='ai')
]
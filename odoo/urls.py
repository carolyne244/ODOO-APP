from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('create_account/', views.create_account, name='create_account'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my_time_off/', views.my_time_off, name='my_time_off'),
    path('time_off_type_form/', views.time_off_type_form, name='time_off_type_form'),
    path('time_off_request_form/', views.time_off_request_form, name='time_off_request_form'),
    path('time_off_allocation_form/', views.time_off_allocation_form, name='time_off_allocation_form'),
    path('my_time_off_table/', views.my_time_off_table, name='my_time_off_table'),
    path('time_off_table/', views.time_off_table, name='time_off_table'),
]

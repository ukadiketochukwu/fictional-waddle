from django.urls import path
from .views import register_view, login_view, logout_view, dashboard_view, index_view,create_truck_view, create_load_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', index_view, name='index'), 
    path('create-truck/', create_truck_view, name='create-truck'),
    path('create-load/', create_load_view, name='create-load'),
]

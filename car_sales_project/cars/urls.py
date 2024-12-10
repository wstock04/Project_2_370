from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('add/', views.add_car, name='add_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
]

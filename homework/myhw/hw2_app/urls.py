from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/<int:user_id>/orders/', views.user_orders, name='user_orders'),
    path('client/<int:client_id>/orders/week/', views.client_orders_week, name='client_orders_week'),
    path('client/<int:client_id>/orders/month/', views.client_orders_month, name='client_orders_month'),
    path('client/<int:client_id>/orders/year/', views.client_orders_year, name='client_orders_year'),
]

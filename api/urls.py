from django.urls import path
from api import views

urlpatterns = [
    path('get_good_receive', views.get_good_receive),
    path('get_delivery_order', views.get_delivery_order),
    path('get_stock_transfer', views.get_stock_transfer),
    path('get_receiving', views.get_receiving),
]

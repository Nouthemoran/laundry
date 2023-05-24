from django.urls import path
from . import views

app_name = 'customer'  # nama aplkasi

urlpatterns = [
    path('customer/create/', views.create_customer, name='create'),
    path('customer/list/', views.customer_list, name='read'),
    path('customer/update/<str:id_cust>/', views.update_customer, name='update'),
    path('customer/delete/<str:id_cust>/', views.delete_customer, name='delete'),
]

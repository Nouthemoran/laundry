from django.urls import path
from . import views

app_name = 'transaksi'  # Nama aplikasi

urlpatterns = [
    path('transaksi/list/', views.transaksi_list, name='read'),
    path('transaksi/create/', views.create_transaksi, name='create'),
    path('transaksi/update/<int:no_faktur>/', views.update_transaksi, name='update'),
    path('transaksi/delete/<int:no_faktur>/', views.delete_transaksi, name='delete'),
]

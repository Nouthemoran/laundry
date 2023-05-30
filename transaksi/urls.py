from django.urls import path
from . import views
from .views import TransaksiPDFView

app_name = 'transaksi'  # Nama aplikasi

urlpatterns = [
    path('transaksi/list/', views.transaksi_list, name='read'),
    path('transaksi/create/', views.create_transaksi, name='create'),
    path('transaksi/update/<int:no_faktur>/', views.update_transaksi, name='update'),
    path('transaksi/delete/<int:no_faktur>/', views.delete_transaksi, name='delete'),
    path('transaksi/detail/<int:no_faktur>/', views.transaksi_detail, name='detail'),
    path('transaksi/detail/<int:no_faktur>/pdf/', TransaksiPDFView.as_view(), name='cetak'),

]

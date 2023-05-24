from django.db import models
from customer.models import Customer 
from user.models import User
# Create your models here.

class Transaksi(models.Model):
    no_faktur = models.IntegerField(primary_key=True)
    id_cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tgl_masuk = models.DateTimeField()
    batas_waktu = models.DateTimeField()
    tgl_bayar = models.DateTimeField(null=True, blank=True)
    jumlah = models.IntegerField()
    harga = models.FloatField()
    STATUS_CHOICES = [
        ('baru', 'Baru'),
        ('proses', 'Proses'),
        ('selesai', 'Selesai'),
        ('diambil', 'Diambil'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    DIBAYAR_CHOICES = [
        ('dibayar', 'Dibayar'),
        ('belum_dibayar', 'Belum Dibayar'),
    ]
    dibayar = models.CharField(max_length=15, choices=DIBAYAR_CHOICES)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    jumlah_bayar = models.FloatField()

    def __str__(self):
        return f"No Faktur: {self.no_faktur}"

 
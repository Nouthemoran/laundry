from django.db import models

# Create your models here.
class Customer(models.Model):
    id_cust = models.CharField(max_length=5, primary_key=True)
    nama_cust = models.CharField(max_length=30)
    alamat = models.TextField()
    hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_cust

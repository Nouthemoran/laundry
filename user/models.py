from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.CharField(max_length=5, primary_key=True)
    nama_user = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nama_user

class Meta:
    permissions = [
        ("Admin", "Can view user"),
    ]

from django import forms
from django.forms import DateTimeInput
from .models import Transaksi

class TransaksiForm(forms.ModelForm):
    class Meta:
        model = Transaksi
        fields = '__all__'
        widgets = {
            'tgl_masuk': DateTimeInput(attrs={'type': 'datetime-local'}),
            'batas_waktu': DateTimeInput(attrs={'type': 'datetime-local'}),
            'tgl_bayar': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('id_cust', 'nama_cust', 'alamat', 'hp')

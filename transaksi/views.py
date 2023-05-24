
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaksi
from .forms import TransaksiForm

def transaksi_list(request):
    transaksis = Transaksi.objects.all()
    return render(request, 'transaksi/transaksi_list.html', {'transaksis': transaksis})

def create_transaksi(request):
    if request.method == 'POST':
        form = TransaksiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaksi:read')
    else:
        form = TransaksiForm()
    return render(request, 'transaksi/create_transaksi.html', {'form': form})

def update_transaksi(request, no_faktur):
    transaksi = get_object_or_404(Transaksi, no_faktur=no_faktur)
    if request.method == 'POST':
        form = TransaksiForm(request.POST, instance=transaksi)
        if form.is_valid():
            form.save()
            return redirect('transaksi:read')
    else:
        form = TransaksiForm(instance=transaksi)
    return render(request, 'transaksi/update_transaksi.html', {'form': form})

def delete_transaksi(request, no_faktur):
    transaksi = get_object_or_404(Transaksi, no_faktur=no_faktur)
    if request.method == 'POST':
        transaksi.delete()
        return redirect('transaksi:read')  # Menggunakan nama rute 'transaksi:transaksi_list'
    return render(request, 'transaksi/delete_transaksi.html', {'transaksi': transaksi})

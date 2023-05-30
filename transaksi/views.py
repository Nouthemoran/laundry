
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaksi
from .forms import TransaksiForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views import View

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

def transaksi_detail(request, no_faktur):
    transaksi = get_object_or_404(Transaksi, no_faktur=no_faktur)
    return render(request, 'transaksi/transaksi_detail.html', {'transaksi': transaksi})

class TransaksiPDFView(View):
    def get(self, request, no_faktur):
        # Mengambil data transaksi berdasarkan nomor faktur
        transaksi = Transaksi.objects.get(no_faktur=no_faktur)
        
        # Render template ke dalam string
        template = 'transaksi_detail.html'
        html_string = render_to_string('transaksi/transaksi_detail.html', {'transaksi': transaksi})

        
        # Membuat HttpResponse dengan tipe konten PDF
        response = HttpResponse(content_type='application/pdf')
        
        # Menentukan nama file PDF yang dihasilkan
        response['Content-Disposition'] = 'attachment; filename="transaksi_detail.pdf"'
        
        # Membuat objek canvas PDF
        p = canvas.Canvas(response)
        
        # Mengonversi template HTML ke dalam file PDF
        p.drawString(100, 700, "Detail Transaksi")
        p.drawString(100, 650, f"No Faktur: {transaksi.no_faktur}")
        p.drawString(100, 600, f"ID Customer: {transaksi.id_cust}")
        p.drawString(100, 550, f"Tanggal Masuk: {transaksi.tgl_masuk}")
        p.drawString(100, 500, f"Batas Waktu: {transaksi.batas_waktu}")
        p.drawString(100, 450, f"Tanggal Bayar: {transaksi.tgl_bayar}")
        p.drawString(100, 400, f"Nama Barang: {transaksi.nama_brg}")
        p.drawString(100, 350, f"Jumlah: {transaksi.jumlah}")
        p.drawString(100, 300, f"Harga: {transaksi.harga}")
        p.drawString(100, 250, f"Status: {transaksi.status}")
        p.drawString(100, 200, f"Dibayar: {transaksi.dibayar}")
        p.drawString(100, 150, f"ID User: {transaksi.id_user}")
        p.drawString(100, 100, f"Jumlah Bayar: {transaksi.jumlah_bayar}")
        # Tambahkan elemen lain sesuai kebutuhan
        
        # Mengakhiri dokumen PDF
        p.showPage()
        p.save()
        
        return response

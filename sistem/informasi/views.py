# informasi/views.py
from django.shortcuts import render
from django.db.models import Sum, Count
from .models import Membeli, DetailPembelian

def laporan_transaksi(request):
    # Laporan total pembelian per pembeli
    total_per_pembeli = Membeli.objects.values('id_pembeli__nama').annotate(
        total_harga_pembelian=Sum('total_harga')
    )

    # Laporan penjualan per barang
    penjualan_per_barang = DetailPembelian.objects.values('idBarang__nama').annotate(
        jumlah_dibeli=Count('idBarang'),
        total_penjualan=Sum('idBarang__harga')
    )

    # Pembelian tertinggi (5 besar)
    pembelian_tertinggi = Membeli.objects.select_related('id_pembeli').order_by('-total_harga')[:5]
    pembelian_tertinggi_data = [
        {
            'pembeli': pembelian.id_pembeli.nama,
            'total_harga': pembelian.total_harga,
            'barang': ", ".join(
                [d.idBarang.nama for d in DetailPembelian.objects.filter(idMembeli=pembelian).select_related('idBarang')]
            ),
        }
        for pembelian in pembelian_tertinggi
    ]

    # Data transaksi dengan tanggal
    pembelian_dengan_tanggal = Membeli.objects.select_related('id_pembeli').order_by('tanggal_pembelian')
    pembelian_dengan_tanggal_data = [
        {
            'pembeli': pembelian.id_pembeli.nama,
            'tanggal': pembelian.tanggal_pembelian,
            'total_harga': pembelian.total_harga,
            'barang': ", ".join(
                [d.idBarang.nama for d in DetailPembelian.objects.filter(idMembeli=pembelian).select_related('idBarang')]
            ),
        }
        for pembelian in pembelian_dengan_tanggal
    ]

    # Kirim data ke template
    context = {
        'total_per_pembeli': total_per_pembeli,
        'penjualan_per_barang': penjualan_per_barang,
        'pembelian_tertinggi': pembelian_tertinggi_data,
        'pembelian_dengan_tanggal': pembelian_dengan_tanggal_data,
    }
    return render(request, 'laporan.html', context)

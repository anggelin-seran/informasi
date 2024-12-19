from django.contrib import admin
from django.urls import path, include
from informasi import views  # Impor views dari aplikasi informasi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('informasi/', include('informasi.urls')),  # Rute untuk aplikasi informasi
    path('laporan/', views.laporan_transaksi, name='laporan'),  # Tambahkan rute untuk laporan
]

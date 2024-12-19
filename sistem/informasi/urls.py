from django.urls import path
from . import views  # Impor views dari aplikasi informasi

urlpatterns = [
    path('laporan/', views.laporan_transaksi, name='laporan-transaksi'),
]

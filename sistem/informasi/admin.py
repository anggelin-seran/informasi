from django.contrib import admin
from informasi.models import pembeli, Barang, Membeli, DetailPembelian
# Register your models here.

admin.site.register(pembeli)
admin.site.register(Barang)
admin.site.register(Membeli)
admin.site.register(DetailPembelian)

from django.db import models

# Create your models here.


class pembeli(models.Model):
    id_pembeli = models.CharField(max_length=50, primary_key=True)
    nama = models.CharField(max_length=50)

    class Meta:
        verbose_name = "pembeli"
        verbose_name_plural = "pembeli"

    def __str__(self):
        return f'id_pembeli:{self.id_pembeli}-nama:{self.nama}'


class Barang(models.Model):
    idBarang = models.CharField(max_length=15, primary_key=True)
    nama = models.CharField(max_length=50)
    harga = models.PositiveIntegerField(verbose_name="harga")

    class Meta:
        verbose_name = "Barang"
        verbose_name_plural = "Barang"

    def __str__(self):
        return f'nama:{self.nama}-harga:{self.harga}'


class Membeli(models.Model):
    id = models.AutoField(primary_key=True)
    id_pembeli = models.ForeignKey(pembeli, on_delete=models.CASCADE)
    total_harga = models.PositiveIntegerField(verbose_name="total_harga")
    tanggal_pembelian = models.DateField(
        verbose_name="Tanggal Pembelian", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Membeli"
        verbose_name_plural = "Membeli"

    def __str__(self):
        return f'idpembeli: {self.id_pembeli}, harga: {self.total_harga}, Tanggal Pembalian: {self.tanggal_pembelian}'


class DetailPembelian(models.Model):
    id = models.AutoField(verbose_name="idDetail", primary_key=True)
    idBarang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    idMembeli = models.ForeignKey(Membeli, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "DetailPembelian"
        verbose_name_plural = "DetailPembelian"

    def __str__(self):
        return f'id_Detail: {self.id}, idBarang: {self.idBarang}, idMembeli: {self.idMembeli}'

# Generated by Django 5.1.2 on 2024-11-14 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informasi', '0005_alter_barang_options_alter_membeli_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membeli',
            name='tanggal_pembelian',
            field=models.DateField(verbose_name='Tanggal Pembelian'),
        ),
    ]

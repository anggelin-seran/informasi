# Generated by Django 5.1.2 on 2024-11-14 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informasi', '0002_alter_barang_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membeli',
            options={'verbose_name': 'Barang', 'verbose_name_plural': 'Barang'},
        ),
        migrations.AlterModelOptions(
            name='pembeli',
            options={'verbose_name': 'pembeli', 'verbose_name_plural': 'pembeli'},
        ),
    ]

# Generated by Django 5.1.2 on 2024-11-19 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informasi', '0007_remove_membeli_idbarang_detailpembelian'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detailpembelian',
            options={'verbose_name': 'DetailPembelian', 'verbose_name_plural': 'DetailPembelian'},
        ),
    ]

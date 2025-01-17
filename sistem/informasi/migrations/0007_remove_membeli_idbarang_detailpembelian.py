# Generated by Django 5.1.2 on 2024-11-14 03:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informasi', '0006_alter_membeli_tanggal_pembelian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membeli',
            name='idBarang',
        ),
        migrations.CreateModel(
            name='DetailPembelian',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='idDetail')),
                ('idBarang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informasi.barang')),
                ('idMembeli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informasi.membeli')),
            ],
            options={
                'verbose_name': 'DetailPembelian',
                'verbose_name_plural': 'DetailPembelians',
            },
        ),
    ]

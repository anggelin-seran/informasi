# Generated by Django 5.1.2 on 2024-11-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informasi', '0003_alter_membeli_options_alter_pembeli_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='membeli',
            name='tanggal_pembelian',
            field=models.DateField(blank=True, null=True, verbose_name='Tanggal Pembelian'),
        ),
    ]

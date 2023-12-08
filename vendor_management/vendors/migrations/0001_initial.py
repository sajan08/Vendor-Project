# Generated by Django 3.0 on 2023-12-08 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('contact_details', models.CharField(max_length=255)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=50)),
                ('order_date', models.DateField()),
                ('items', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('status', models.CharField(max_length=20)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.Vendor')),
            ],
        ),
    ]

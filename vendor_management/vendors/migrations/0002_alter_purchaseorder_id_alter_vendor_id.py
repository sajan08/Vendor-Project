# Generated by Django 5.0 on 2023-12-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vendors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseorder",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]

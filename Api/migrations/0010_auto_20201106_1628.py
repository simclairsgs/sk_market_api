# Generated by Django 3.1.2 on 2020-11-06 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_tax_tax_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='Billing_Employee',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='billing',
            name='Products',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='billing',
            name='Timestamp',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_Name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Product_Name',
            field=models.CharField(max_length=25),
        ),
    ]

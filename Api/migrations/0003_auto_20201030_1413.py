# Generated by Django 3.1.2 on 2020-10-30 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_billing_login_sales_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='Mobile_Number',
            field=models.IntegerField(),
        ),
    ]

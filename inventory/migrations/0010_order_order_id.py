# Generated by Django 4.2.5 on 2024-04-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_order_invoice_status_order_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(default=1111, max_length=4, unique=True),
            preserve_default=False,
        ),
    ]

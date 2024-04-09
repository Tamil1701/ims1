# Generated by Django 4.2.5 on 2024-04-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_order_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_status',
            field=models.CharField(choices=[('not_generated', 'Not Generated'), ('generated', 'Generated')], default='not_generated', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=20),
        ),
    ]

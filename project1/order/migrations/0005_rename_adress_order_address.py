# Generated by Django 4.2.5 on 2023-09-12 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_rename_orders_orderproduct_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adress',
            new_name='address',
        ),
    ]
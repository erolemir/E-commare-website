# Generated by Django 4.2.5 on 2023-09-09 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contactformmessage_alter_setting_aboutus_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactformmessage',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=10),
        ),
    ]

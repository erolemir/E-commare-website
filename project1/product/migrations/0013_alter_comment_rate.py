# Generated by Django 4.2.5 on 2023-09-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-11 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

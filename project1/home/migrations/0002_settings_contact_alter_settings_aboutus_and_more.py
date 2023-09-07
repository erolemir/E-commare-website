# Generated by Django 4.2.5 on 2023-09-07 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='settings',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='settings',
            name='referances',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtpemail',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtppassword',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='settings',
            name='smtpserver',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-27 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_aboutus_alter_companyinfo_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='description',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='title',
        ),
    ]
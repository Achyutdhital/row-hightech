# Generated by Django 4.2.5 on 2023-10-01 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_productcategoryitems_main_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-01 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_enquiry_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='product',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]

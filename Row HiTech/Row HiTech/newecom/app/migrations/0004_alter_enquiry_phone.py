# Generated by Django 4.2.5 on 2023-09-26 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_message_enquiry_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
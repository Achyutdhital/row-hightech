# Generated by Django 4.2.5 on 2023-09-26 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_enquiry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enquiry',
            old_name='message',
            new_name='comment',
        ),
    ]

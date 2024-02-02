# Generated by Django 4.2.5 on 2023-09-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdsImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.PositiveIntegerField()),
                ('ads_Img', models.ImageField(upload_to='adsImg/')),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
    ]

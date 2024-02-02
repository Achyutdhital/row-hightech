# Generated by Django 4.2.5 on 2023-09-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_aboutus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.PositiveIntegerField()),
                ('slider_img', models.ImageField(upload_to='slider/')),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
    ]
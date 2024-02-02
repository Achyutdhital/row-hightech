# Generated by Django 4.2.5 on 2023-09-26 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.PositiveIntegerField()),
                ('message', models.TextField()),
                ('product_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app.productcategoryitems')),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-29 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_enquiry_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='product_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_title', to='app.productcategoryitems'),
        ),
    ]

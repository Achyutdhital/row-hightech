# Generated by Django 4.2.5 on 2023-09-29 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_remove_productimage_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategoryitems',
            name='main_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main_category', to='app.mainproductcategory'),
            preserve_default=False,
        ),
    ]

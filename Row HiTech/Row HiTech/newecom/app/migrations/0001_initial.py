# Generated by Django 4.2.5 on 2023-09-26 05:21

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1024)),
                ('main_ctg_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='product_name', unique=True)),
                ('order_number', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('description', ckeditor.fields.RichTextField()),
                ('order_number', models.PositiveIntegerField()),
                ('last_ctg_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('order_number', models.PositiveIntegerField()),
                ('ctg_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='app.mainproductcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='productImg/')),
                ('last_sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='app.productcategoryitems')),
            ],
        ),
        migrations.AddField(
            model_name='productcategoryitems',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_sub_categories', to='app.subproductcategory'),
        ),
    ]
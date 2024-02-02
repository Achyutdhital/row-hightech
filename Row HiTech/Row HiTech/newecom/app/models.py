from django.db import models

# Create your models here.
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.

class MainProductCategory(models.Model):
    product_name = models.CharField(max_length=1024)
    main_ctg_slug = AutoSlugField(populate_from='product_name', unique=True)
    order_number = models.PositiveIntegerField()
    
    class Meta:
        ordering = ['id']
        
    def __str__(self):
        return self.product_name
    
class SubProductCategory(models.Model):
    title = models.CharField(max_length=1000)
    main_category = models.ForeignKey(MainProductCategory, on_delete=models.CASCADE, related_name='sub_categories')
    order_number = models.PositiveIntegerField()
    ctg_slug = AutoSlugField(populate_from='title', unique=True)
    
    def __str__(self):
        return self.title
    


class ProductCategoryItems(models.Model):
    name = models.CharField(max_length=1000)
    main_category = models.ForeignKey(MainProductCategory, on_delete=models.CASCADE, related_name='main_category')
    sub_category = models.ForeignKey(SubProductCategory, on_delete=models.CASCADE, related_name='last_sub_categories')
    description = RichTextField()
    order_number = models.PositiveIntegerField()
    last_ctg_slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    last_sub_category = models.ForeignKey(ProductCategoryItems, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='productImg/')

    def __str__(self):
        return str(self.image)
    
    
class Enquiry(models.Model):
    product= models.CharField(max_length=1000)
    name= models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    message=models.TextField()
    
class ContactUs(models.Model):
    product= models.CharField(max_length=1000)
    name= models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.PositiveIntegerField()
    message=models.TextField()
    
    
class CompanyInfo(models.Model):
    location=models.CharField(max_length=1000)
    facebook_link= models.URLField(blank=True, null=True)
    youtube_link= models.URLField(max_length=1000, blank=True, null=True)
    instagram_link=models.URLField(blank=True, null=True)
    location_link=models.URLField(max_length=1000,blank=True, null=True)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField()
    logo=models.ImageField(upload_to='logo/')
    
class AboutUs(models.Model):
    messageMD=RichTextField()
    mdName=models.CharField(max_length=200)
    mdImage=models.ImageField(upload_to='mdImage/')
    
    
class Slider(models.Model):
    order_number=models.PositiveIntegerField()
    slider_img=models.ImageField(upload_to="slider/")
    
class BannerImg(models.Model):
    order_number=models.PositiveIntegerField()
    banner_Img=models.ImageField(upload_to="adsImg/")


class Ecatelog(models.Model):
    order_number=models.PositiveIntegerField()
    title=models.CharField(max_length=1000)
    eCatelog=models.URLField(max_length=10000)

from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(MainProductCategory)
class MainProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'order_number')
    # Add any other customizations you need

@admin.register(SubProductCategory)
class SubProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'main_category')
    # Add any other customizations you need

from django.contrib import admin
from .models import ProductCategoryItems, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # Number of empty image fields to display (you can adjust this)

class ProductCategoryItemsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'sub_category','order_number')  # Customize the list display columns
    list_filter = ('sub_category',)  # Add filters if needed
    search_fields = ('name',)  # Add search fields if needed

    inlines = [ProductImageInline]  # Include the ProductImage model inline

admin.site.register(ProductCategoryItems, ProductCategoryItemsAdmin)


@admin.register(Enquiry)
class EnquiryyAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','message')
    # Add any other customizations you need'
    

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','phone','message')
    # Add any other customizations you need
    
@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('id','phone','email','location','logo','facebook_link','youtube_link','instagram_link','location_link')
    
@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id','messageMD','mdName','mdImage')
    
    
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','slider_img')
    
@admin.register(BannerImg)
class BannerImgAdmin(admin.ModelAdmin):
    list_display = ('id','banner_Img')
    
@admin.register(Ecatelog)
class EcatelogAdmin(admin.ModelAdmin):
    list_display = ('id','eCatelog')
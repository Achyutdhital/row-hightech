from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import *


app_name ='dashboard'
urlpatterns = [
        path('',views.index,name='index'),
        path('login', views.login, name='login'),
        path('logout', views.userlogout, name='logout'),
        path('about-us', views.aboutUs, name='aboutUs'),

        path('companyinfo', views.companyinfo, name='companyinfo'),

        path('deleteeCatelog/<int:id>/',views.deleteeCatelog,name='deleteeCatelog'),
        path('eCatelog',views.eCatelog,name='eCatelog'),

        path('deletecontactUs/<int:id>/',views.deletecontactUs,name='deletecontactUs'),
        path('contact',views.contactUs,name='contactUs'),

        path('deleteenquiry/<int:id>/',views.deleteenquiry,name='deleteenquiry'),
        path('enquiry',views.enquiry,name='enquiry'),

        path('add_slider_image',views.add_edit_sliderImage,name='add_slider_image'),
        path('edit_slider_image/<int:id>/',views.add_edit_sliderImage,name='edit_slider_image'),
        path('deletesliderImg/<int:id>/',views.deletesliderImg,name='deletesliderImg'),
        path('sliderImg',views.sliderImg,name='sliderImg'),
        
        path('add_Banner',views.add_edit_Banner,name='add_Banner'),
        path('edit_Banner/<int:id>/',views.add_edit_Banner,name='edit_Banner'),
        path('deleteBanner/<int:id>/',views.deleteBanner,name='deleteBanner'),
        path('Banner',views.Banner,name='Banner'),

        
        path('add_eCatelog',views.add_edit_eCatelog,name='add_eCatelog'),
        path('edit_eCatelog/<int:id>/',views.add_edit_eCatelog,name='edit_eCatelog'),
        
        
        path('add_MainProductCategory',views.add_edit_MainProductCategory,name='add_MainProductCategory'),
        path('edit_MainProductCategory/<int:id>/',views.add_edit_MainProductCategory,name='edit_MainProductCategory'),
        path('deletemainCategory/<int:id>/',views.deletemainCategory,name='deletemainCategory'),
        path('mainCategory',views.mainCategory,name='mainCategory'),

        
        path('add_SubProductCategory',views.add_edit_SubProductCategory,name='add_SubProductCategory'),
        path('edit_SubProductCategory/<int:id>/',views.add_edit_SubProductCategory,name='edit_SubProductCategory'),
        path('deletesubCategory/<int:id>/',views.deletesubCategory,name='deletesubCategory'),
        path('subCategory',views.subCategory,name='subCategory'),

        
        path('add_ProductCategoryItems',views.add_ProductCategoryItems,name='add_ProductCategoryItems'),
        # path('edit_ProductCategoryItems/<int:id>/',views.add_ProductCategoryItems,name='edit_ProductCategoryItems'),
        path('deleteproductItems/<int:id>/',views.deleteproductItems,name='deleteproductItems'),
        path('productItems',views.productItems,name='productItems'),
        path('subcategories', views.load_sub_category, name="ajax_load_courses"),
      
        
        path('change_password/', views.change_password, name='change_password'),
        


]+ static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
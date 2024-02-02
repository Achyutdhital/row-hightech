from django.urls import path, include
from . import views
from .views import *
from .views import product_description 

app_name="app"

urlpatterns = [ 
    path('', views.index, name="index"),
    path('allCategory/', views.allCategory, name="allCategory"),
    path('about/', views.about, name="about"),
    path('product_categories_view/', views.product_categories_view, name="product_categories_view"),
    path('productDetails/', views.productDetails, name="productDetails"),
    path('product/<slug:slug>', views.product,name='product'),
    path('product_description/<slug:slug>', views.product_description,name='product_description'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('slider', views.slider, name='slider'),
    path('eCatelog', views.eCatelog, name='eCatelog'),
    path('product/<str:slug>/', product_description, name='product_description'),

    
]
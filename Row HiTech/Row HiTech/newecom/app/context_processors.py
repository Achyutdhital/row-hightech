from .models import *
from django.core.paginator import Paginator


def main_categories(request):
    main_categories = MainProductCategory.objects.order_by('order_number')
    last_sub_categories = ProductCategoryItems.objects.order_by('order_number')
    p=Paginator(last_sub_categories,9)
    page_number= request.GET.get('page')
    last_sub_categories=p.get_page(page_number)
    return {'main_categories': main_categories,'last_sub_category':last_sub_categories,'product':last_sub_categories}


def companyInfo(request):
    companyinfo = CompanyInfo.objects.first()
    return {'companyinfo':companyinfo}

def slider(request):
    slider = Slider.objects.all().order_by('-id')
    return {'slider':slider}

def bannerImg(request):
    bannerImg = BannerImg.objects.all().order_by('-id')
    return {'bannerImg':bannerImg}
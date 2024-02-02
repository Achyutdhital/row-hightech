from django.shortcuts import render,HttpResponse, HttpResponseRedirect,redirect,get_object_or_404
from account.models import User
from django.contrib.auth import authenticate, login, logout
from . decorators import login_required
from django.contrib import messages
from django.contrib import auth
from . forms import *
from app.models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator
from . new_file_handler import validate_file
from django.http import JsonResponse


def login(request):
    try:
        if request.user.is_authenticated:
            return render(request,'app2/index.html')
        if request.method =="POST":
            email = request.POST['useremail']
            print(email)
            password = request.POST['password']
            print(password)
            # user_obj = User.objects.filter(email=email)
            user_obj = authenticate(email=email, password=password)
            print(user_obj)
            if not user_obj: #not user_obj.exists():
                messages.warning(request,"Invalid username and password...")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            user_obj = authenticate(email=email, password=password)
            if user_obj and user_obj.is_superuser or user_obj.is_editor:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            messages.warning(request,'Inavlid Password')
            return redirect('dashboard:login')
        return render(request,'app2/login.html')
    except Exception as e:
        print(e)
        messages.warning(request,'something wrong...')
        return redirect('dashboard:login')

@login_required
def userlogout(request):
    auth.logout(request)
    messages.info(request,"logout successfully..")
    return redirect('dashboard:login')


@login_required
def index(request):
    return render(request,'app2/index.html')


@login_required
def aboutUs(request):
    instance = None
    try:
        if id:
            instance = AboutUs.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the aboutUs.')
        return redirect('dashboard:aboutUs')

    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'aboutUs edited successfully.')
                return redirect('dashboard:aboutUs')  # Redirect to the edited aboutUs's details page
            else:  # Add operation
                messages.success(request, 'aboutUs added successfully.')
                return redirect('dashboard:aboutUs')  # Redirect to the page for adding new aboutUss
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutUsForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_about_us.html', context)

@login_required
def companyinfo(request):
    instance = None
    try:
        if id:
            instance = CompanyInfo.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the companyinfo.')
        return redirect('dashboard:companyinfo')

    if request.method == 'POST':
        form = CompanyInfoForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'companyinfo edited successfully.')
                return redirect('dashboard:companyinfo')  # Redirect to the edited companyinfo's details page
            else:  # Add operation
                messages.success(request, 'companyinfo added successfully.')
                return redirect('dashboard:companyinfo')  # Redirect to the page for adding new companyinfos
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = CompanyInfoForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_companyinfo.html', context)


# #news categorei
@login_required
def add_edit_sliderImage(request, id=None):
    instance = None
    try:
        if id:
            instance = Slider.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the slider Image.')
        return redirect('dashboard:add_slider_image')

    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'slider Image edited successfully.')
                return redirect('dashboard:edit_slider_image', id=instance.id)  # Redirect to the edited slider Image's details page
            else:  # Add operation
                messages.success(request, 'slider Image added successfully.')
                return redirect('dashboard:add_slider_image')  # Redirect to the page for adding new slider Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = SliderForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_sliderImage.html', context)


@login_required
def add_edit_Banner(request, id=None):
    instance = None
    try:
        if id:
            instance = BannerImg.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Banner Image.')
        return redirect('dashboard:add_Banner')

    if request.method == 'POST':
        form = BannerImgForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Banner Image edited successfully.')
                return redirect('dashboard:edit_Banner', id=instance.id)  # Redirect to the edited Banner Image's details page
            else:  # Add operation
                messages.success(request, 'Banner Image added successfully.')
                return redirect('dashboard:add_Banner')  # Redirect to the page for adding new Banner Images
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = BannerImgForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Banner.html', context)


@login_required
def add_edit_eCatelog(request, id=None):
    instance = None
    try:
        if id:
            instance = Ecatelog.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the eCatelog.')
        return redirect('dashboard:add_eCatelog')

    if request.method == 'POST':
        form = EcatelogForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'eCatelog edited successfully.')
                return redirect('dashboard:edit_eCatelog', id=instance.id)  # Redirect to the edited eCatelog's details page
            else:  # Add operation
                messages.success(request, 'eCatelog added successfully.')
                return redirect('dashboard:add_eCatelog')  # Redirect to the page for adding new eCatelogs
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = EcatelogForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_eCatelog.html', context)


@login_required
def add_edit_MainProductCategory(request, id=None):
    instance = None
    try:
        if id:
            instance = MainProductCategory.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the MainProductCategory.')
        return redirect('dashboard:add_MainProductCategory')

    if request.method == 'POST':
        form = MainProductCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'MainProductCategory edited successfully.')
                return redirect('dashboard:edit_MainProductCategory', id=instance.id)  # Redirect to the edited MainProductCategory's details page
            else:  # Add operation
                messages.success(request, 'MainProductCategory added successfully.')
                return redirect('dashboard:add_MainProductCategory')  # Redirect to the page for adding new MainProductCategorys
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = MainProductCategoryForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_MainProductCategory.html', context)


@login_required
def add_edit_SubProductCategory(request, id=None):
    instance = None
    try:
        if id:
            instance = SubProductCategory.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the SubProductCategory.')
        return redirect('dashboard:add_SubProductCategory')

    if request.method == 'POST':
        form = SubProductCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'SubProductCategory edited successfully.')
                return redirect('dashboard:edit_SubProductCategory', id=instance.id)  # Redirect to the edited SubProductCategory's details page
            else:  # Add operation
                messages.success(request, 'SubProductCategory added successfully.')
                return redirect('dashboard:add_SubProductCategory')  # Redirect to the page for adding new SubProductCategorys
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = SubProductCategoryForm(instance=instance)

    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_SubProductCategory.html', context)


from .forms import ProductCategoryItemsForm, ProductImageFormSet

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProductCategoryItemsForm, ProductImageFormSet

def add_ProductCategoryItems(request):
    allcategorie= MainProductCategory.objects.all()
    user= request.user
    if request.method=="POST":
        maincategorie = MainProductCategory.objects.get(id= request.POST['main_category'])
        subcategorie = SubProductCategory.objects.get(id=request.POST['sub_category'])
        form = ProductCategoryItemsForm(request.POST)

        if form.is_valid():
            product_instance = form.save(commit=False)
            product_instance.main_category = maincategorie
            product_instance.sub_category= subcategorie
            product_instance.save()
            formset = ProductImageFormSet(request.POST, request.FILES) 
            
            if formset.is_valid():
                for product_image_form in formset:
                    if product_image_form.cleaned_data.get('image'):
                        images = request.FILES.getlist('image')  # Get a list of uploaded image files

                        for image_file in images:
                            image_instance = ProductImage(product=product_instance, image=image_file)
                            image_instance.save()
            else:
                print(formset.errors)
            messages.success(request,'Product added successfully !')
            return redirect('dashboard:add_ProductCategoryItems')
        

        else:
            print(form.errors)
            return HttpResponse(form.errors)

    else:
        form = ProductCategoryItemsForm()
        formset=ProductImageFormSet()
        return render(request,'app2/add_ProductCategoryItems.html',{'allcategorie':allcategorie,
                                                       'user':user,
                                                       'form':form,
                                                       'formset':formset
                                                       })
def load_sub_category(request):
    main_ctg_id = request.GET.get('programming')
    sub_category = SubProductCategory.objects.filter(main_category=main_ctg_id)
    return render(request,'app2/listdropdow.html',{'sub_category':sub_category})

@login_required
def mainCategory(request):
    mainCategory=MainProductCategory.objects.all()
    p=Paginator(mainCategory,10)
    page_number= request.GET.get('page')
    mainCategory=p.get_page(page_number)
    return render(request, 'app2/mainCategory.html',{'details':mainCategory})

@login_required
def deletemainCategory(request, id):
    record = get_object_or_404(MainProductCategory, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:mainCategory')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/mainCategory.html', {'details': record})


@login_required
def subCategory(request):
    subCategory=SubProductCategory.objects.all()
    p=Paginator(subCategory,10)
    page_number= request.GET.get('page')
    subCategory=p.get_page(page_number)
    return render(request, 'app2/subCategory.html',{'details':subCategory})

@login_required
def deletesubCategory(request, id):
    record = get_object_or_404(SubProductCategory, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:subCategory')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/subCategory.html', {'details': record})



@login_required
def productItems(request):
    productItems=ProductCategoryItems.objects.all()
    p=Paginator(productItems,10)
    page_number= request.GET.get('page')
    productItems=p.get_page(page_number)
    return render(request, 'app2/productItems.html',{'details':productItems})

@login_required
def deleteproductItems(request, id):
    record = get_object_or_404(ProductCategoryItems, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:productItems')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/productItems.html', {'details': record})




@login_required
def Banner(request):
    Banner=BannerImg.objects.all()
    p=Paginator(Banner,10)
    page_number= request.GET.get('page')
    Banner=p.get_page(page_number)
    return render(request, 'app2/Banner.html',{'details':Banner})

@login_required
def deleteBanner(request, id):
    record = get_object_or_404(BannerImg, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:Banner')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/Banner.html', {'details': record})



@login_required
def sliderImg(request):
    sliderImg=Slider.objects.all()
    p=Paginator(sliderImg,10)
    page_number= request.GET.get('page')
    sliderImg=p.get_page(page_number)
    return render(request, 'app2/sliderImg.html',{'details':sliderImg})

@login_required
def deletesliderImg(request, id):
    record = get_object_or_404(Slider, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:sliderImg')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/sliderImg.html', {'details': record})




@login_required
def eCatelog(request):
    eCatelog=Ecatelog.objects.all()
    p=Paginator(eCatelog,10)
    page_number= request.GET.get('page')
    eCatelog=p.get_page(page_number)
    return render(request, 'app2/eCatelog.html',{'details':eCatelog})

@login_required
def deleteeCatelog(request, id):
    record = get_object_or_404(Ecatelog, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:eCatelog')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/eCatelog.html', {'details': record})


@login_required
def contactUs(request):
    contactUs=ContactUs.objects.all()
    p=Paginator(contactUs,10)
    page_number= request.GET.get('page')
    contactUs=p.get_page(page_number)
    return render(request, 'app2/contactUs.html',{'details':contactUs})

@login_required
def deletecontactUs(request, id):
    record = get_object_or_404(ContactUs, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:contactUs')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/contactUs.html', {'details': record})


def enquiry(request):
    enquiry=Enquiry.objects.all()
    p=Paginator(enquiry,10)
    page_number= request.GET.get('page')
    enquiry=p.get_page(page_number)
    return render(request, 'app2/enquiry.html',{'details':enquiry})

@login_required
def deleteenquiry(request, id):
    record = get_object_or_404(Enquiry, id=id)

    if request.method == 'POST':
        record.delete()
        return redirect('dashboard:enquiry')  # Redirect to a list view after deletion
    else:
        return render(request, 'app2/enquiry.html', {'details': record})




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # update_session_auth_hash(request, user)  # Important to update the session after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard:change_password')  # Redirect to the same view after successful password change
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'app2/change_password.html', {'form': form})


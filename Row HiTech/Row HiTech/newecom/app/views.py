from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from . models import *
from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.core.mail import send_mail  

# Create your views here.


def index(request):
    is_index_page = True
    return render(request,'app/index.html')

def productDetails(request):
    return render(request,'app/productDetails.html')


def allCategory(request):
    product= ProductCategoryItems.objects.all().order_by('-id')
    p=Paginator(product,2)
    page_number= request.GET.get('page')
    product=p.get_page(page_number)
    return render(request,'app/allCategory.html',{'product':product})

def about(request):
    about=AboutUs.objects.all()
    return render(request,'app/about.html',{'about':about})

def slider(request):
    return render(request,'app/slider.html')

def eCatelog(request):
    catelog=Ecatelog.objects.all().order_by('-id')
    p=Paginator(catelog,6)
    page_number= request.GET.get('page')
    catelog=p.get_page(page_number)
    return render(request,'app/eCatelog.html',{'catelog':catelog})

def product_categories_view(request):
    main_categories = MainProductCategory.objects.all().order_by('-id')
    context = {'main_categories': main_categories}
    return render(request, 'product_categories.html', context)

def product(request,slug):
    data= SubProductCategory.objects.get(ctg_slug=slug)
    products=ProductCategoryItems.objects.filter(sub_category=data.id)
    p=Paginator(products,9)
    page_number= request.GET.get('page')
    products=p.get_page(page_number)
    # data= ProductCategoryItems.objects.get(last_ctg_slug=slug)
    return render(request, 'app/selectedproduct.html',{'data':data,'sub_category':products})

def product_description(request,slug):
    data= ProductCategoryItems.objects.get(last_ctg_slug=slug)
    product = get_object_or_404(ProductCategoryItems, last_ctg_slug=slug)
    related_products = ProductCategoryItems.objects.filter(sub_category=product.sub_category).exclude(last_ctg_slug=slug)
    return render(request, 'app/productDetails.html',{'data':data,'product': product, 'related_products': related_products})

def enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:productDetails')  # Redirect to a success page or another URL
    else:
        form = EnquiryForm()
    
    return render(request, 'app/productDetails.html', {'form': form})
from django.http import HttpResponseServerError

# def enquiry(request):
#     try:
#         if request.method == 'POST':
#             form = EnquiryForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Enquiry added successfully.')
#                 return redirect('app:productDetails')
#             else:
#                 messages.warning(request, 'Form is not valid. Please correct the errors.')
#         else:
#             form = EnquiryForm()

#         details = Enquiry.objects.all()
#         context = {'form': form, 'details': details}
#         return render(request, 'app/productDetails.html', context)

#     except Exception as e:
#         # Log the exception or handle it according to your application's needs
#         messages.error(request, 'An error occurred while processing the enquiry.')
#         return HttpResponseServerError('Internal Server Error')
# def enquiry(request):
#     instance = None
#     try:
#         if id:
#             instance = Enquiry.objects.first()
#     except Exception as e:
#         messages.warning(request, 'An error occurred while retrieving the productDetails.')
#         return redirect('app:enquiry')

#     if request.method == 'POST':
#         form = EnquiryForm(request.POST, request.FILES, instance=instance)
#         if form.is_valid():
#             form.save()
#             if instance:  # Edit operation
#                 messages.success(request, 'productDetails edited successfully.')
#                 return redirect('app:enquiry')  # Redirect to the edited productDetails's details page
#             else:  # Add operation
#                 messages.success(request, 'productDetails added successfully.')
#                 return redirect('app:enquiry')  # Redirect to the page for adding new productDetailss
#         else:
#             messages.warning(request, 'Form is not valid. Please correct the errors.')
#     else:
#         form = EnquiryForm(instance=instance)

#     context = {'form': form, 'instance': instance}
#     print(form.errors)
#     return render(request, 'app/product.html', context)




# def contactUs(request):
#     if request.method == 'POST':
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#             return redirect('app:contactUs')  # Redirect to a success page or another URL
#     else:
      
#         form = ContactUsForm()
    
#     return render(request, 'app/contactUs.html', {'form': form})



# def enquiry(request):
#     enquiries = Enquiry.objects.all()  # Use a different variable name to avoid conflict
    
#     if request.method == "POST":
#         name = request.POST['name']
#         product_title = request.POST['product_title']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         comment = request.POST['comment']
      
#         enquiry_info = Enquiry(product_title=product_title, name=name, phone=phone, email=email, comment=comment)
#         enquiry_info.save()
        
        
#         # Send confirmation email to the user
#         user_subject = "Thank you for contacting us"
#         user_comment = f"Thank you for contacting us.\n" \
#                        f"• Name: {name}\n" \
#                        f"• Phone: {phone}\n" \
#                        f"• Email: {email}\n" \
#                        f"• Comment: {comment}"
#         user_email_from = settings.EMAIL_HOST_USER
#         user_recipient_list = [email]
#         send_mail(user_subject, user_comment, user_email_from, user_recipient_list)
        
#         # Send notification email to the admin
#         admin_subject = "New Contact Form Submission"
#         admin_comment = f"A new contact form has been submitted:\n" \
#                         f"• Name: {name}\n" \
#                         f"• Phone: {phone}\n" \
#                         f"• Email: {email}\n" \
#                         f"• Comment: {comment}"
#         admin_email_from = settings.EMAIL_HOST_USER
#         admin_recipient_list = ["rmshthapa1@gmail.com"]  # Replace with the admin's email address
#         send_mail(admin_subject, admin_comment, admin_email_from, admin_recipient_list)
        
#         messages.success(request, "Thank you for contacting us. We will get back to you via email.")
#         return redirect('app:productDetails') 
#     return render(request, 'app/productDetails.html', {'enquiries': enquiries})
# # Make sure to import send_mail

def contactUs(request):
    contactUs = ContactUs.objects.all()
    categories = MainProductCategory.objects.all()
    
    if request.method == "POST":
        product = request.POST['product']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
      
        contactUs_info = ContactUs(product=product,
                                   name=name,
                                   phone=phone,
                                   email=email,
                                   message=message)
        contactUs_info.save()
        
        # Send confirmation email to the user
        user_subject = "Thank you for contacting us"
        user_message = f"Thank you for contacting us.\n" \
                       f"• Product: {product}\n" \
                       f"• Name: {name}\n" \
                       f"• Phone: {phone}\n" \
                       f"• Email: {email}\n" \
                       f"• Message: {message}"
        user_email_from = settings.EMAIL_HOST_USER
        user_recipient_list = [email]
        send_mail(user_subject, user_message, user_email_from, user_recipient_list)
        
        # Send notification email to the admin
        admin_subject = "New Contact Form Submission"
        admin_message = f"A new contact form has been submitted:\n" \
                        f"• Product: {product}\n" \
                        f"• Name: {name}\n" \
                        f"• Phone: {phone}\n" \
                        f"• Email: {email}\n" \
                        f"• Message: {message}"
        admin_email_from = settings.EMAIL_HOST_USER
        admin_recipient_list = ["rmshthapa1@gmail.com"]  # Replace with the admin's email address
        send_mail(admin_subject, admin_message, admin_email_from, admin_recipient_list)
        
        messages.success(request, "Thank you for contacting us. We will get back to you via email.")
    
    return render(request, 'app/contactUs.html', {'contactUs': contactUs,'categories': categories})



# def enquiry(request):
#     enquiry = Enquiry.objects.all()
#     categories = MainProductCategory.objects.all()
    
#     if request.method == "POST":
#         product = request.POST['product']
#         name = request.POST['name']
#         phone = request.POST['phone']
#         email = request.POST['email']
#         message = request.POST['message']
      
#         enquiry_info = Enquiry(product=product,
#                                    name=name,
#                                    phone=phone,
#                                    email=email,
#                                    message=message)
#         enquiry_info.save()
        
#         # Send confirmation email to the user
#         user_subject = "Thank you for contacting us"
#         user_message = f"Thank you for contacting us.\n" \
#                        f"• Product: {product}\n" \
#                        f"• Name: {name}\n" \
#                        f"• Phone: {phone}\n" \
#                        f"• Email: {email}\n" \
#                        f"• Message: {message}"
#         user_email_from = settings.EMAIL_HOST_USER
#         user_recipient_list = [email]
#         send_mail(user_subject, user_message, user_email_from, user_recipient_list)
        
#         # Send notification email to the admin
#         admin_subject = "New Contact Form Submission"
#         admin_message = f"A new contact form has been submitted:\n" \
#                         f"• Product: {product}\n" \
#                         f"• Name: {name}\n" \
#                         f"• Phone: {phone}\n" \
#                         f"• Email: {email}\n" \
#                         f"• Message: {message}"
#         admin_email_from = settings.EMAIL_HOST_USER
#         admin_recipient_list = ["rmshthapa1@gmail.com"]  # Replace with the admin's email address
#         send_mail(admin_subject, admin_message, admin_email_from, admin_recipient_list)
        
#         messages.success(request, "Thank you for contacting us. We will get back to you via email.")
    
#     return render(request, 'app/productDetails.html', {'enquiry': enquiry,'categories': categories})


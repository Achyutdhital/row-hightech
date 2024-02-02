from django import forms
from app.models import *
from ckeditor.fields import RichTextField
# from ckeditor.widgets import CKEditorWidget
# from ckeditor_uploader.widgets import CKEditorUploadingWidget


# class MainCategorieForm(forms.ModelForm):
#     class Meta:
#         model = MainCategorie
#         fields = '__all__'

# class SubCategorieForm(forms.ModelForm):
#     class Meta:
#         model = SubCategorie
#         fields = '__all__'


class EcatelogForm(forms.ModelForm):
    class Meta:
        model = Ecatelog
        fields = '__all__'

# forms.py
from django.forms import inlineformset_factory


class ProductCategoryItemsForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryItems
        fields = ['name', 'sub_category', 'description', 'order_number']

ProductImageFormSet = inlineformset_factory(ProductCategoryItems, ProductImage, fields=['image'],  
        widgets = {'image': forms.ClearableFileInput(attrs={'required': 'required','class': 'form-control'}),
        }, extra=1)


class SubProductCategoryForm(forms.ModelForm):
    class Meta:
        model = SubProductCategory
        fields = '__all__'

class MainProductCategoryForm(forms.ModelForm):
    class Meta:
        model = MainProductCategory
        fields = '__all__'

class BannerImgForm(forms.ModelForm):
    class Meta:
        model = BannerImg
        fields = '__all__'

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
        
class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = '__all__'


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields ='__all__'
        
# class DigitalMarketingForm(forms.ModelForm):
#     description = forms.CharField(widget=CKEditorUploadingWidget())
#     class Meta:
#         model = DigitalMarketing
#         fields ='__all__'
#         # description = forms.CharField(widget=forms.Textarea)

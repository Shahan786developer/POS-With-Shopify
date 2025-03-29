from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

##################
# Add Category FOrm
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'code', 'description', 'category_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),   
          'description': forms.Textarea(attrs={'class': 'form-control'}),
          'category_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),    
        }
###################
# Brand Form

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'description', 'brand_image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
              
          'description': forms.Textarea(attrs={'class': 'form-control'}),
          'brand_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),    
        }

###################################

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['parent_category', 'subcategory_name', 'code', 'description']
        widgets = {
            'parent_category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory_name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

            
        }
        ##########################


class TaxForm(forms.ModelForm):
    class Meta:
        model = TaxModel
        fields = ['name', 'rate', 'status']


class DiscountForm(forms.ModelForm):
    class Meta:
        model = DiscountModel
        fields = ['name', 'rate', 'status']

#################

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'subcategory',
                  'brand', 'unit', 'sku','min_qty', 'quantity', 'description',
                  'tax', 'discount_type', 'price','product_image','status'
                  ]
      
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'unit': forms.Select(attrs={'class': 'form-select'}),
            'sku': forms.TextInput(attrs={'class': 'form-control'}),
            'minimum_qty': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'tax': forms.Select(attrs={'class': 'form-select'}),
            'discount_type': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

      
     
    
from django.db import models
from django.contrib.auth.models import User
# # Create your models here.

# #################################################
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=15)  
    description = models.TextField(null=True, blank=True)
    category_image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    class Meta:
        unique_together = ['user' ,'code']

    def __str__(self):
        return self.name
    
###########################################
# #Subcategory
##############################################

class SubCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)
    class Meta:
        unique_together = ['user' ,'code']

    def __str__(self):
        return self.subcategory_name

# ##############################
#Brand Model
########################################
class Brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    brand_image = models.ImageField(upload_to='brand_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    #####################################
    # Tex Model

  
#######################################
class TaxModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    
    TAX_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    ]

    name = models.CharField(max_length=255, verbose_name='Tax Name')
    rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Tax Rate (%)')
    status = models.CharField(max_length=10, choices=TAX_STATUS_CHOICES, verbose_name='Status')

    def __str__(self):
       return f"{self.name} - {self.rate}%"
 ########################################### 
class DiscountModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    
    Discount_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    ]

    name = models.CharField(max_length=255, verbose_name='Discount Name')
    rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Discount Rate (%)')
    status = models.CharField(max_length=10, choices=Discount_STATUS_CHOICES, verbose_name='Status')

    def __str__(self):
         return f"{self.name} - {self.rate}%"

############ Product ###############


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='User')
    name = models.CharField(max_length=255, verbose_name='Product Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True,blank=True ,verbose_name='Sub Category')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brand',null=True,blank=True)

    UNIT_CHOICES = [
        ('Each (EA)', 'Each (EA)'),
        ('Kilogram (KG)', 'Kilogram (KG)'),
        ('Gram (G)', 'Gram (G)'),
        ('Liter (L)', 'Liter (L)'),
        ('Milliliter (ML)', 'Milliliter (ML)'),
        ('Meter (M)', 'Meter (M)'),
        ('Centimeter (CM)', 'Centimeter (CM)'),
        ('Square Meter (M²)', 'Square Meter (M²)'),
        ('Cubic Meter (M³)', 'Cubic Meter (M³)'),
        ('Pack (PK)', 'Pack (PK)'),
        ('Pair (PR)', 'Pair (PR)'),
        ('Box (BX)', 'Box (BX)'),
        ('Case (CS)', 'Case (CS)'),
        ('Dozen (DOZ)', 'Dozen (DOZ)'),
        ('Bundle (BUN)', 'Bundle (BUN)'),
    ]
    
    unit = models.CharField(max_length=40, choices=UNIT_CHOICES, verbose_name='Unit')
    sku = models.CharField(max_length=15, verbose_name='SKU')
    
    min_qty = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Minimum Qty')
    
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Quantity')
    
    description = models.TextField(verbose_name='Description')
    
    tax = models.ForeignKey(TaxModel, on_delete=models.CASCADE, verbose_name='Tax',null=True,blank=True)

    discount_type = models.ForeignKey(DiscountModel, on_delete=models.CASCADE, verbose_name='Discount Type',null=True,blank=True)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    ]
    product_image = models.ImageField(upload_to='product_images/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Status')
    class Meta:
        unique_together = ['user' ,'name','sku']
    def __str__(self):
        return self.name





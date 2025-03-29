from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from requests import request
from .forms import *
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm 
# Create your views here.
def index(request):

    return render(request,'posapp/index.html')

@login_required
def dashboard(request):

    return render(request,'posapp/dashboard.html')
 # Import your custom form

def register(request): 
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect('/user/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


#  from here our other files functions starts 


def activities_view(request):
    return render(request, 'posapp/activities.html')

def add_sales_view(request):
    return render(request, 'posapp/add-sales.html')

def addbrand_view(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES or None)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            print(brand)
            brand.save()
            
            return redirect('brandlist')  # Redirect to a brand list view
    else:
        form = BrandForm()
    return render(request, 'posapp/addbrand.html',{'form': form})

def addcategory_view(request):
    user = request.user
    if request.method == 'POST': 
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
           
            code = form.cleaned_data['code']
            
            if Category.objects.filter(user=user,code=code).exists():
                # Handle the uniqueness constraint violation
                form.add_error(None, f"A product with the same Category Code already exists for {user}")

            else:
             category = form.save(commit=False)
             category.user = request.user  # Assign the user to the category
             category.save()
             return redirect('categorylist')  # Redirect to a category list view
        # Handle the case when the form is not valid (e.g., form errors)
        # You can add error handling or redirect back to the form with error messages.
    else:
        form = CategoryForm()
    
    return render(request, 'posapp/addcategory.html', {'form': form})

def addcustomer_view(request):
    return render(request, 'posapp/addcustomer.html')

def addproduct_view(request):
    user = request.user
    categories = Category.objects.filter(user=user)

    subcategories= SubCategory.objects.filter(user=user)
    brands = Brand.objects.filter(user=user)
    units = Product.UNIT_CHOICES
    
    taxes= TaxModel.objects.filter(user=user)
    discounts= DiscountModel.objects.filter(user=user)
 
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            sku = form.cleaned_data['sku']
            
            if Product.objects.filter(user=user, name=name, sku=sku).exists():
                # Handle the uniqueness constraint violation
                form.add_error(None, f"A product with the same name and SKU already exists for {user}")

            else:
                
                brand = form.save(commit=False)
                brand.user = request.user
           
                brand.save()
                return redirect('productlist')
            
            
            
    else:
        form = ProductForm()
    context = {'categories':categories,'subcategories':subcategories,'brands':brands,
                'units': units,'taxes': taxes, 'discounts':discounts
                ,'form':form} 

    return render(request, 'posapp/addproduct.html',context)

def addpurchase_view(request):
    return render(request, 'posapp/addpurchase.html')

def addquotation_view(request):
    return render(request, 'posapp/addquotation.html')

def addstore_view(request):
    return render(request, 'posapp/addstore.html')

def addsupplier_view(request):
    return render(request, 'posapp/addsupplier.html')

def addtransfer_view(request):
    return render(request, 'posapp/addtransfer.html')

def adduser_view(request):
    return render(request, 'posapp/adduser.html')

def barcode_view(request):
    return render(request, 'posapp/barcode.html')

def blankpage_view(request):
    return render(request, 'posapp/blankpage.html')

def brandlist_view(request):
    brands = Brand.objects.all()
    return render(request, 'posapp/brandlist.html', {'brands': brands})

def calendar_view(request):
    return render(request, 'posapp/calendar.html')

def categorylist_view(request):
     user = request.user
     
     categories = Category.objects.filter(user = user) 
     context = {'categories': categories}
     return render(request, 'posapp/categorylist.html',context=context)

def chart_apex_view(request):
    return render(request, 'posapp/chart-apex.html')

def chart_flot_view(request):
    return render(request, 'posapp/chart-flot.html')

def chart_js_view(request):
    return render(request, 'posapp/chart-js.html')

def chart_morris_view(request):
    return render(request, 'posapp/chart-morris.html')

def chart_peity_view(request):
    return render(request, 'posapp/chart-peity.html')

def chat_view(request):
    return render(request, 'posapp/chat.html')

def clipboard_view(request):
    return render(request, 'posapp/clipboard.html')

def components_view(request):
    return render(request, 'posapp/components.html')

def contact_view(request):
    return render(request, 'posapp/contact.html')

def counter_view(request):
    return render(request, 'posapp/counter.html')

def countrieslist_view(request):
    return render(request, 'posapp/countrieslist.html')

def createexpense_view(request):
    return render(request, 'posapp/createexpense.html')

def createpermission_view(request):
    return render(request, 'posapp/createpermission.html')

def createpurchasereturn_view(request):
    return render(request, 'posapp/createpurchasereturn.html')

def createsalesreturn_view(request):
    return render(request, 'posapp/createsalesreturn.html')

def createsalesreturns_view(request):
    return render(request, 'posapp/createsalesreturns.html')

def currencysettings_view(request):
    return render(request, 'posapp/currencysettings.html')

def customerlist_view(request):
    return render(request, 'posapp/customerlist.html')

def customerreport_view(request):
    return render(request, 'posapp/customerreport.html')

def dashboard_view(request):
    return render(request, 'posapp/dashboard.html')

def data_tables_view(request):
    return render(request, 'posapp/data-tables.html')

def drag_drop_view(request):
    return render(request, 'posapp/drag-drop.html')

def edit_sales_view(request):
    return render(request, 'posapp/edit-sales.html')

def editbrand_view(request,pk):
    return render(request, 'posapp/editbrand.html')

class UpdateBrandView(View):
    template_name = 'posapp/editbrand.html'
   
    def get(self, request, pk):
        brand = get_object_or_404(Brand, id=pk,user = request.user)
        form = BrandForm(instance=brand)
        image_url = brand.brand_image.url if brand.brand_image else None


        context = {'form': form,'image_url': image_url }
        
        return render(request, self.template_name, context)

    def post(self, request, pk):
        brand = get_object_or_404(Brand, id=pk,user = request.user)
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            
            form.save()
            return redirect('brandlist')
        
                
        return render(request, self.template_name, )


def editcategory_view(request,pk):
    return render(request, 'posapp/editcategory.html')
class UpdateCategoryView(View):
    template_name = 'posapp/editcategory.html'
   
    def get(self, request, pk):
        category = get_object_or_404(Category, id=pk,user = request.user)
        form = CategoryForm(instance=category)
        
        image_url = category.category_image.url if category.category_image else None


        context = {'form': form,'image_url': image_url }
        
        return render(request, self.template_name, context)

    def post(self, request, pk):
        category = get_object_or_404(Category, id=pk,user = request.user)
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            
            form.save()
            return redirect('categorylist')
        
        
                
        return render(request, self.template_name)

def editcountry_view(request):
    return render(request, 'posapp/editcountry.html')

def editcustomer_view(request):
    return render(request, 'posapp/editcustomer.html')

def editexpense_view(request):
    return render(request, 'posapp/editexpense.html')

def editpermission_view(request):
    return render(request, 'posapp/editpermission.html')


class UpdateProductView(View):
    template_name = 'posapp/editproduct.html'
   
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk,user = request.user)
        form = ProductForm(instance=product)
        user = request.user
        categories = Category.objects.filter(user=user)
        
        
        subcategories= SubCategory.objects.filter(user=user)
        brands = Brand.objects.filter(user=user)
        units = Product.UNIT_CHOICES
        status= Product.STATUS_CHOICES
        product_instance = Product.objects.get(id=pk)
        taxes= TaxModel.objects.filter(user=user)
        discounts= DiscountModel.objects.filter(user=user)
        context = {'form': form, 'action': 'Update','categories':categories,'subcategories':subcategories,'brands':brands,
                'units': units,'taxes': taxes, 'discounts':discounts,'status':status,'image_url': product_instance.product_image.url
                ,}
        
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk, user=request.user)
        form = ProductForm(request.POST, request.FILES, instance=product)
        categories = Category.objects.filter(user=request.user)
        if form.is_valid():
            name = form.cleaned_data['name']
            sku = form.cleaned_data['sku']
            user = request.user
            #products_with_same_sku = Product.objects.filter(user=user, name=name, sku=sku).exclude(id=pk)

            # if products_with_same_sku.exists() and not Product.objects.filter(user=user, name=name, sku=sku).exclude(id=pk).exists():
            #     # Handle the uniqueness constraint violation
            #     form.add_error(None, f"A product with the same name or SKU already exists for {user}")

            # else:
            form.save()
            return redirect('product-details', product_id=pk)
        user = request.user
        categories = Category.objects.filter(user=user)

        subcategories= SubCategory.objects.filter(user=user)
        brands = Brand.objects.filter(user=user)
        units = Product.UNIT_CHOICES
        status= Product.STATUS_CHOICES
        product_instance = Product.objects.get(id=pk)

    # Pass the image URL to the template
       
        taxes= TaxModel.objects.filter(user=user)
        discounts= DiscountModel.objects.filter(user=user)
        context = {'form': form, 'action': 'Update','categories':categories,'subcategories':subcategories,'brands':brands,
                'units': units,'taxes': taxes, 'discounts':discounts,'status':status,'image_url': product_instance.product_image.url
                ,}
        return render(request, self.template_name, context)

def editpurchase_view(request):
    return render(request, 'posapp/editpurchase.html')

def editpurchasereturn_view(request):
    return render(request, 'posapp/editpurchasereturn.html')

def editquotation_view(request):
    return render(request, 'posapp/editquotation.html')

def editsalesreturn_view(request):
    return render(request, 'posapp/editsalesreturn.html')

def editsalesreturns_view(request):
    return render(request, 'posapp/editsalesreturns.html')

def editstate_view(request):
    return render(request, 'posapp/editstate.html')

def editstore_view(request):
    return render(request, 'posapp/editstore.html')

def editsubcategory_view(request,pk):
    return render(request, 'posapp/editsubcategory.html')


class UpdateSubCategoryView(View):
    template_name = 'posapp/editsubcategory.html'
   
    def get(self, request, pk):
        subcategory = get_object_or_404(SubCategory, id=pk,user = request.user)
        form = SubCategoryForm(instance=subcategory)
        Categories = Category.objects.filter(user=request.user)

        categories = SubCategory.objects.filter(user=request.user)
        
        
        context = {'form': form, 'categories':categories,'Categories':Categories
                }
        
        return render(request, self.template_name, context)

    def post(self, request, pk):
        subcategory = get_object_or_404(SubCategory, id=pk, user=request.user)
        form = SubCategoryForm(request.POST, instance=subcategory)
        categories = SubCategory.objects.filter(user=request.user)
        if form.is_valid():
            
           
            form.save()
            return redirect('subcategorylist')
        user = request.user
        categories = SubCategory.objects.filter(user=user)


    # Pass the image URL to the template
        form = SubCategoryForm()
        context = {'form': form, 'action': 'Update','categories':categories,}
        return render(request, self.template_name, context)


def editsupplier_view(request):
    return render(request, 'posapp/editsupplier.html')

def edittransfer_view(request):
    return render(request, 'posapp/edittransfer.html')

def edituser_view(request):
    return render(request, 'posapp/edituser.html')

def email_view(request):
    return render(request, 'posapp/email.html')

def emailsettings_view(request):
    return render(request, 'posapp/emailsettings.html')

def error_404_view(request):
    return render(request, 'posapp/error-404.html')

def error_500_view(request):
    return render(request, 'posapp/error-500.html')

def expensecategory_view(request):
    return render(request, 'posapp/expensecategory.html')

def expenselist_view(request):
    return render(request, 'posapp/expenselist.html')

def forgetpassword_view(request):
    return render(request, 'posapp/forgetpassword.html')

def form_basic_inputs_view(request):
    return render(request, 'posapp/form-basic-inputs.html')

def form_fileupload_view(request):
    return render(request, 'posapp/form-fileupload.html')

def form_horizontal_view(request):
    return render(request, 'posapp/form-horizontal.html')

def form_input_groups_view(request):
    return render(request, 'posapp/form-input-groups.html')

def form_mask_view(request):
    return render(request, 'posapp/form-mask.html')

def form_select2_view(request):
    return render(request, 'posapp/form-select2.html')

def form_validation_view(request):
    return render(request, 'posapp/form-validation.html')

def form_vertical_view(request):
    return render(request, 'posapp/form-vertical.html')

def form_wizard_view(request):
    return render(request, 'posapp/form-wizard.html')

def generalsettings_view(request):
    return render(request, 'posapp/generalsettings.html')

def grouppermissions_view(request):
    return render(request, 'posapp/grouppermissions.html')

def icon_feather_view(request):
    return render(request, 'posapp/icon-feather.html')

def icon_flag_view(request):
    return render(request, 'posapp/icon-flag.html')

def icon_fontawesome_view(request):
    return render(request, 'posapp/icon-fontawesome.html')

def icon_ionic_view(request):
    return render(request, 'posapp/icon-ionic.html')

def icon_material_view(request):
    return render(request, 'posapp/icon-material.html')

def icon_pe7_view(request):
    return render(request, 'posapp/icon-pe7.html')

def icon_simpleline_view(request):
    return render(request, 'posapp/icon-simpleline.html')

def icon_themify_view(request):
    return render(request, 'posapp/icon-themify.html')

def icon_typicon_view(request):
    return render(request, 'posapp/icon-typicon.html')

def icon_weather_view(request):
    return render(request, 'posapp/icon-weather.html')

def importproduct_view(request):
    return render(request, 'posapp/importproduct.html')

def importpurchase_view(request):
    return render(request, 'posapp/importpurchase.html')

def importtransfer_view(request):
    return render(request, 'posapp/importtransfer.html')

def index_view(request):
    return render(request, 'posapp/index.html')

def inventoryreport_view(request):
    return render(request, 'posapp/inventoryreport.html')

def invoicereport_view(request):
    return render(request, 'posapp/invoicereport.html')

def lightbox_view(request):
    return render(request, 'posapp/lightbox.html')

def newcountry_view(request):
    return render(request, 'posapp/newcountry.html')

def newstate_view(request):
    return render(request, 'posapp/newstate.html')

def newuser_view(request):
    return render(request, 'posapp/newuser.html')

def newuseredit_view(request):
    return render(request, 'posapp/newuseredit.html')

def notification_view(request):
    return render(request, 'posapp/notification.html')

def paymentsettings_view(request):
    return render(request, 'posapp/paymentsettings.html')

def popover_view(request):
    return render(request, 'posapp/popover.html')

def pos_view(request):
    return render(request, 'posapp/pos.html')

def product_details_view(request, product_id):
    product = Product.objects.get(id=product_id,user = request.user)  # Assuming you have a Product model
    return render(request, 'posapp/product-details.html',{'product':product})

def productlist_view(request):
    user = request.user
    products = Product.objects.filter(user=user)

    context = {
        'products': products,
    }
    return render(request, 'posapp/productlist.html',context)

def profile_view(request):
    return render(request, 'posapp/profile.html')

def purchaselist_view(request):
    return render(request, 'posapp/purchaselist.html')

def purchaseorderreport_view(request):
    return render(request, 'posapp/purchaseorderreport.html')

def purchasereport_view(request):
    return render(request, 'posapp/purchasereport.html')

def purchasereturnlist_view(request):
    return render(request, 'posapp/purchasereturnlist.html')

def quotationList_view(request):
    return render(request, 'posapp/quotationList.html')

def rangeslider_view(request):
    return render(request, 'posapp/rangeslider.html')

def rating_view(request):
    return render(request, 'posapp/rating.html')

def ribbon_view(request):
    return render(request, 'posapp/ribbon.html')

def sales_details_view(request):
    return render(request, 'posapp/sales-details.html')

def saleslist_view(request):
    return render(request, 'posapp/saleslist.html')

def salesreport_view(request):
    return render(request, 'posapp/salesreport.html')

def salesreturnlist_view(request):
    return render(request, 'posapp/salesreturnlist.html')

def salesreturnlists_view(request):
    return render(request, 'posapp/salesreturnlists.html')

def scrollbar_view(request):
    return render(request, 'posapp/scrollbar.html')

def signin_view(request):
    return render(request, 'posapp/signin.html')

def signup_view(request):
    return render(request, 'posapp/signup.html')

def spinner_view(request):
    return render(request, 'posapp/spinner.html')

def statelist_view(request):
    return render(request, 'posapp/statelist.html')

def stickynote_view(request):
    return render(request, 'posapp/stickynote.html')

def storelist_view(request):
  
    return render(request, 'posapp/storelist.html')



def subaddcategory_view(request):
    user = request.user
    categories = Category.objects.filter(user = user)
    
    if request.method == 'POST':
        form = SubCategoryForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            
            if SubCategory.objects.filter(user=user,code=code).exists():
                # Handle the uniqueness constraint violation
                form.add_error(None, f"A product with the same SubCategory Code already exists for {user}")

            else:

              brand = form.save(commit=False)
              brand.user = request.user
            
              brand.save()
              return redirect('subcategorylist')  # Change 'subcategory_list' to the URL name of the subcategory list page.
    else:
        form = SubCategoryForm()
    
    context = {'form': form, 'categories': categories}
    return render(request, 'posapp/subaddcategory.html', context)


def subcategorylist_view(request):
    user = request.user
    # categories = Category.objects.filter(user=user)
    subcategories = SubCategory.objects.filter(user=user)
    
    return render(request, 'posapp/subcategorylist.html', { 'subcategories': subcategories})
   

def supplierlist_view(request):
    return render(request, 'posapp/supplierlist.html')

def supplierreport_view(request):
    return render(request, 'posapp/supplierreport.html')

def sweetalerts_view(request):
    return render(request, 'posapp/sweetalerts.html')

def tables_basic_view(request):
    return render(request, 'posapp/tables-basic.html')
class UpdateTaxView(View):
    template_name = 'posapp/taxrates.html'

    def get(self, request, pk):
        tax = get_object_or_404(TaxModel, id=pk, user=request.user)
        form = TaxForm(instance=tax)
        context = {'form': form, 'tax': tax}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        tax = get_object_or_404(TaxModel, id=pk, user=request.user)
        form = TaxForm(request.POST, instance=tax)
        if form.is_valid():
            form.save()
            return redirect('taxrates')  # Redirect to the appropriate page after update
        context = {'form': form, 'tax': tax}
        return render(request, self.template_name, context)
def taxrates_view(request, pk=None):
    user = request.user
    taxes = TaxModel.objects.filter(user=user)

    # If pk is provided, it means we are updating an existing tax
    if pk:
        tax = get_object_or_404(TaxModel, id=pk, user=user)
    else:
        tax = None

    if request.method == 'POST':
        if tax:
            form = TaxForm(request.POST, instance=tax)
        else:
            form = TaxForm(request.POST)

        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            # Redirect to a success page or tax list page.
            return redirect('taxrates')  # Change 'taxrates' to the URL name of the tax list page.
    else:
        form = TaxForm(instance=tax)

    context = {'form': form, 'taxes': taxes}
    return render(request, 'posapp/taxrates.html', context)
def discountrates_view(request):
     discounts = DiscountModel.objects.all()
     if request.method == 'POST':
        form = DiscountForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
           
            brand.save()
            # Redirect to a success page or tax list page.
            return redirect('discountrates')  # Change 'tax_list' to the URL name of the tax list page.
     else:
        form = DiscountForm()

     context = {'form': form,'discounts': discounts}

     return render(request, 'posapp/discount.html',context)

def text_editor_view(request):
    
     return render(request, 'posapp/text-editor.html')
    

def timeline_view(request):
    return render(request, 'posapp/timeline.html')

def toastr_view(request):
    return render(request, 'posapp/toastr.html')

def tooltip_view(request):
    return render(request, 'posapp/tooltip.html')

def transferlist_view(request):
    return render(request, 'posapp/transferlist.html')

def userlist_view(request):
    return render(request, 'posapp/userlist.html')

def userlists_view(request):
    return render(request, 'posapp/userlists.html')


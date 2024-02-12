from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views import View
import razorpay
from. models import Dress
from . forms import CustomerRegistrationForms,CustomerProfileForm
from django.contrib import messages
from . models import Customer,Cart
from django.db.models import Q
from django.conf import settings

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')




class CategoryView(View):
    def get(self,request,val):
     dress = Dress.objects.filter(category=val)
     title = Dress.objects.filter(category=val).values('title')
     return render(request,'app/category.html',locals())
 
 
class DressDetail(View):
    def get (self,request,pk):
         dress = Dress.objects.get(pk=pk)
         return render(request,'app/dressdetail.html',locals())
     
     
class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForms()
        return render(request, 'app/customerregistration.html',locals())
    def post(self,request):
       form = CustomerRegistrationForms(request.POST) 
       if form.is_valid():
          form.save()
          messages.success(request,"Congratuations! User Register Successfully") 
       else:
           messages.warning(request,"Invalid Input Data") 
       return render(request, 'app/customerregistration.html',locals())
   
   
class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user,name=name,mobile=mobile,locality=locality,city=city,zipcode=zipcode)
            reg.save()
            messages.success(request,"Congratulation! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return render(request, 'app/profile.html',locals())
    
    
    
def address(request):
    add = Customer.objects.filter(user=request.user) 
    return render(request, 'app/address.html',locals())

class UpdateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form =CustomerProfileForm(instance=add)
        return render(request, 'app/updateaddress.html',locals())
        
    def post(self,request,pk):
        form =CustomerProfileForm(request.POST)
        if form.is_valid():
            add= Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"Congratulation! Profile Save Successfully")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')
    
def add_to_cart(request):
    user  = request.user
    dress_id=request.GET.get('dre_id') 
    dress = Dress.objects.get(id=dress_id) 
    Cart(user=user,dress=dress).save()
    return redirect('/cart')

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0
    for p in cart:
        value = p.quantity * p.dress.discounted_price
        amount = amount + value 
    totalamount = amount + 40
    return render(request, 'app/addtocart.html',locals())

class Checkout(View):
    def get(self,request):
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_item=Cart.objects.filter(user=user)
        famount = 0
        for p in cart_item:
            value = p.quantity * p.dress.discounted_price
            famount = famount + value
        totalamount = famount + 40
        return render (request, 'app/checkout.html',locals())
    


def plus_cart(request):
    if request.method == 'GET':
        dre_id=request.GET['dre_id']
        c = Cart.objects.get(Q(dress=dre_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.dress.discounted_price
            amount = amount + value
        totalamount = amount + 40
        #print(dre_id)
        data={  
              'quantity':c.quantity,
              'amount' :amount,
              'totalamount' :totalamount 
        }
        return JsonResponse(data)
    
    
def minus_cart(request):
    if request.method == 'GET':
        dre_id=request.GET['dre_id']
        c = Cart.objects.get(Q(dress=dre_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.dress.discounted_price
            amount = amount + value
        totalamount = amount + 40
        #print(dre_id)
        data={  
              'quantity':c.quantity,
              'amount' :amount,
              'totalamount' :totalamount 
        }
        return JsonResponse(data)
    
    
def remove_cart(request):
    if request.method == 'GET':
        dre_id=request.GET['dre_id']
        c = Cart.objects.get(Q(dress=dre_id) & Q(user=request.user))
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.dress.discounted_price
            amount = amount + value
        totalamount = amount + 40
        #print(dre_id)
        data={  
              'amount' :amount,
              'totalamount' :totalamount 
        }
        return JsonResponse(data)
       
       
       
       

    
      
    
    
    
    
       
       
         
        
   
   
   
        
          
 
        
from django.contrib import admin
from . models import Dress,Customer,Cart,Payment,OrderPlaced 




@admin.register(Dress)
class DressModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','discounted_price','category','dress_image']
    
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','locality','mobile','city','zipcode']
    
   
@admin.register(Cart) 
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','dress','quantity']   
    

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id','paid']  
    
@admin.register(OrderPlaced)
class OrderPlaceModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','dress','quantity','ordered_date','status','payment']
    






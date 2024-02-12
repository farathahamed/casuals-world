from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES={
    ('JN','jeans'),
    ('CFRT','casual-full-sleeve-round-neck-Tshirts'),
    ('CHCT','casual-half-sleeve-collar-Tshirts'),
    ('CHRT','casual-half-sleeve-round-neck-Tshirts'),
    ('CHS','casual-half-size-shirts'),
    ('CFS','casual-full-size-shirts'),
}



class Dress(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField() 
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=4)
    dress_image = models.ImageField(upload_to='dress')
    def __str__(self):
        return self.title
    
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    dress = models.ForeignKey(Dress,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    @property
    def total_cost(self):
        return self.quantity * self.dress.discounted_price
    
    
STATUS_CHOICES = {
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
    
     
 }   
    
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=False)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=False)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=False)
    paid = models.BooleanField(default=False)

    
class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    dress = models.ForeignKey(Dress,on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.dress.discounted_price
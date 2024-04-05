from django.db import models
from category.models import Category
from size.models import Size
from type.models import Type
from customers.models import Customer

class Product(models.Model):
    name = models.CharField(max_length=100)
    # type = models.ManyToManyField(Type, null=True, blank=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images/')
    price = models.IntegerField()
    details = models.TextField()
    quantity = models.IntegerField()
    size = models.ManyToManyField(Size, null=True, blank=True)
    color = models.CharField(max_length=20)
    code = models.CharField(max_length=10)
    wishlist = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    Customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)
    review = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    ratings = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Customer : {self.Customer.user.username} ; Product {self.Product.user.name}"

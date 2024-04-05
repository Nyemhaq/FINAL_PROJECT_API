from django.db import models
from django.contrib.auth.models import User

STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='customers/images/')
    mobile_no = models.CharField(max_length = 12)
    address = models.CharField(max_length=100)
    ratings = models.CharField(choices = STAR_CHOICES, max_length = 10)
    reviews = models.TextField()
    # wishlist = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    

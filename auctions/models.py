from django.contrib.auth.models import AbstractUser,User
from django.db import models

class User(AbstractUser):
    pass
    
class bidding(models.Model):
    start = models.IntegerField()
    bid= models.IntegerField(default=0, blank=True)
   
    money = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE,related_name="money")
    def __str__(self):
        return f"{self.start}"

class categories(models.Model):
    types = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.types}"
class listing(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    title = models.CharField(max_length=64)
    image = models.URLField()
    des = models.CharField(max_length=100)
    bids = models.OneToOneField(bidding, on_delete=models.CASCADE, related_name = "bids")
    category = models.ForeignKey(categories,on_delete=models.CASCADE,related_name = "category")
    winner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="winner", null = True, blank=True,default="")
    def __str__(self):
        return f"{self.id}. {self.title}"

class comment(models.Model):
    com = models.CharField(max_length=300)
    product = models.ForeignKey(listing,on_delete=models.CASCADE, related_name = "product")
    person = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "person")
    def __str__(self):
        return f"{self.com} "
class watchlist(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "users")
    items = models.ManyToManyField(listing, blank=True, related_name="items")
    def __str__(self):
        return f"{self.users}"
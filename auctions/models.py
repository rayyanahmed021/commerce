from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
    
class bidding(models.Model):
    bid= models.IntegerField()
    def __str__(self):
        return f"{self.bid}"
class listing(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    title = models.CharField(max_length=64)
    image = models.URLField()
    des = models.CharField(max_length=100)
    bids = models.OneToOneField(bidding, on_delete=models.CASCADE, related_name = "bids")
    def __str__(self):
        return f"{self.id}. {self.title}"

class watchlist(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "users")
    items = models.ManyToManyField(listing,related_name="items")
    def __str__(self):
        return f"{self.users}"
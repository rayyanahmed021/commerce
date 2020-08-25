from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass
class listing(models.Model):
    created = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created")
    title = models.CharField(max_length=64)
    image = models.URLField()
    des = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.title}"
class bidding(models.Model):
    bid= models.IntegerField()
    def __str__(self):
        return f"{self.bid}"
class watchlist(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE, related_name = "users")
    item = models.ForeignKey(listing,on_delete=models.CASCADE,related_name="item")
    items = models.ManyToManyField(listing, related_name="items")
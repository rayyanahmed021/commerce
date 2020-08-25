from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models.functions import Replace

from .models import User,listing,watchlist,bidding

def watch(request,listing_id):
    c = listing.objects.get(pk = listing_id)
    d = c.items.all()
    list = []
    for names in d:
        list.append(names)
        if user.username in list:

            return render(request,"auctions/listing.html",{
                "list":list,
                "auction":c,
                "message":"c",
                "user":User.username
                })
        else:
            pass
        
def index(request):
    return render(request, "auctions/index.html",{
        "auction": listing.objects.all(),
        "bids":bidding.objects.all()
    })
def listings(request,listing_id):
    c = listing.objects.get(pk = listing_id)
    d = c.items.all()
    list = []
    for names in d:
        list.append(names)
    if request.method == "POST" :
        if User.username in list:
            return render(request,"auctions/listing.html",{
                "list":list,
                "auction":c,
                "message":"c",
                "user":User.username
                })
        byde = bidding.objects.get(pk = listing_id)
        bids = request.POST["biddings"]
        c = listing.objects.get(pk = listing_id)
        d = watchlist.objects.get(item=c.title)
        
        if int(f"{bids}") > int(f"{byde}") :
            bidding.objects.update(bid=Replace("bid",int(f"{byde}"),int(f"{bids}")))
            return render(request, "auctions/listing.html",{
                "auction":listing.objects.get(pk=listing_id),
                "bids": bidding.objects.get(pk = listing_id),
                "list":list,
                "user":User.username
            })
        else:
            return render(request,"auctions/listing.html",{
                "auction": listing.objects.get(pk=listing_id),
                "bids":bidding.objects.get(pk = listing_id),
                "list":list,
                "user":User.username
                })
    return render(request, "auctions/listing.html",{
    "auction":listing.objects.get(pk=listing_id),
    "bids": bidding.objects.get(pk =listing_id),
    "list":list,
    "user":User.username
    }) 
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

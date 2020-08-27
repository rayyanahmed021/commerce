from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models.functions import Replace

from .models import User,listing,watchlist,bidding,categories,comment



def watchlists(request,username):    
    f = User.objects.get(username = username)        
    usery = watchlist.objects.get(users= f.id )
    return render(request,"auctions/index.html",{
        "auction":usery.items.all()
        })


def watch(request,listing_id,username):
    if request.method == "POST":
        c = listing.objects.get(pk = listing_id)
        d = c.items.all()
        f = User.objects.get(username = username)
        
        usery = watchlist.objects.get(users= f.id )
        list = []
        for names in d:
            list.append(names)
        if username in list.__str__() :
            usery.items.remove(c)
            
            return HttpResponseRedirect(reverse("listings", args = (listing_id,)))
        else:
            usery.items.add(c)
            return HttpResponseRedirect(reverse("listings", args = (listing_id,)))
    return HttpResponseRedirect(reverse("listings", args = (listing_id,)))

def create(request,username):
    if request.method == "POST":
        users = User.objects.get(username=username)
        title = request.POST["Title"]
        bid = request.POST["Bid"]
        bydes = bidding(bid=int(f"{bid}"))
        bydes.save()
        description  = request.POST["Description"]
        image = request.POST["image"]
        f = listing(created=users,title=title, image=image, des= description, bids=bydes)
        f.save() 
        return render(request, "auctions/create.html",{
        "message":"c"
        })
    return render(request,"auctions/create.html")




def index(request):
    return render(request, "auctions/index.html",{
        "auction": listing.objects.all()
            })
def listings(request,listing_id):
    c = listing.objects.get(pk = listing_id)
    d = c.items.all()
    list = []
    

    if request.method == "POST" :
        byde = bidding.objects.get(pk = listing_id)
        bids = request.POST.get("biddingss",0) 
               
        if int(f"{bids}") > int(f"{byde}"):
            bidding.objects.update(bid=Replace("bid",int(f"{byde}"),int(f"{bids}")))
            return render(request, "auctions/listing.html",{
                    "auction":c,
                    "success":"u"
                    })
        else:
            return render(request,"auctions/listing.html",{
                    "auction": c,
                    "error":"u"
                   
                    })
    for names in d:
        list.append(names)    
    return render(request, "auctions/listing.html",{
            "auction":c,
            "list": list.__str__()
            
                }) 
def close(request,listing_id):
    c = listing.objects.get(pk = listing_id)
    return render(request,"auctions/listing.html",{
        "auction":c
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

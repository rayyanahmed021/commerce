from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db.models.functions import Replace
from django.contrib.auth.decorators import login_required

from .models import User,listing,watchlist,bidding,categories,comment

def lis(request,listing_id):
    c = listing.objects.get(pk = listing_id)
    d = c.items.all()
    list = []
    for names in d:
        list.append(names)    

    return render(request, "auctions/listing.html",{
        "auction":c,
            "list": list.__str__(),
            "comments": comment.objects.filter(product=c),
            "bid":bidding.objects.get(pk = listing_id )

    })
@login_required()
def watchlists(request,username):    
    f = User.objects.get(username = username)        
    usery = watchlist.objects.get(users= f.id )
    return render(request,"auctions/index.html",{
        "auction":usery.items.all(),
        "message":"c"
        })

@login_required()
def watch(request,listing_id):
    if request.method == "POST":
        c = listing.objects.get(pk = listing_id)
        d = c.items.all()
        usernamy = request.POST.get("username",0)
        f = User.objects.get(username = usernamy)
        
        usery = watchlist.objects.get(users= f.id )
        list = []
        for names in d:
            list.append(names)
        if username in list.__str__() :
            usery.items.remove(c)
            
            return HttpResponseRedirect(reverse("dis", args = (listing_id,)))
        else:
            usery.items.add(c)
            return HttpResponseRedirect(reverse("dis", args = (listing_id,)))
    return HttpResponseRedirect(reverse("dis", args = (listing_id,)))
@login_required()
def create(request,username):
    if request.method == "POST":
        users = User.objects.get(username=username)
        title = request.POST["Title"]
        category = request.POST["category"]
        d = categories.objects.get(types=category)
        bid = request.POST["Bid"]
        bydes = bidding(start=int(f"{bid}"), bid=0)
        bydes.save()
        description  = request.POST["Description"]
        image = request.POST["image"]
        f = listing(created=users,title=title, image=image, des= description, bids=bydes,category=d)
        f.save() 
        return render(request, "auctions/create.html",{
        "message":"c"
        })
    return render(request,"auctions/create.html")
@login_required()
def commy(request,listing_id):
    if request.method == "POST":
        comy = request.POST["comments"]
        usernamy = request.POST.get("username",0)

        f = comment(com = comy , product=listing.objects.get(pk = listing_id), person = User.objects.get(username = usernamy))
        f.save()
        return HttpResponseRedirect(reverse("dis", args = (listing_id,)))


def index(request):
    return render(request, "auctions/index.html",{
        "auction": listing.objects.all()
            })

@login_required()
def listings(request,listing_id):
    c = listing.objects.get(pk = listing_id)
    d = c.items.all()
    list = []
    

    if request.method == "POST" :
        byde = bidding.objects.get(pk = listing_id)
        bids = request.POST.get("biddingss",0) 
        comments = request.POST.get("comment",0)
        usernamy = request.POST.get("username",0)      
        if int(f"{bids}") > int(f"{byde.start}") and int(f"{bids}")> int(f"{byde.bid}"):
            byde.bid = bids
            byde.money = User.objects.get(username = usernamy)
            byde.save()
            for names in d:
                list.append(names)
            
            return render(request, "auctions/listing.html",{
                    "auction":c,
                    "success":"u",
                    "bid":bidding.objects.get(pk = listing_id ),
                    "comments": comment.objects.filter(product=c),
                    "list": list.__str__()
                    })
        else:
            for names in d:
                list.append(names)
            return render(request,"auctions/listing.html",{
                    "auction": c,
                    "error":"u",
                    "list": list.__str__(),
                    "bid":bidding.objects.get(pk = listing_id ),
                    "comments": comment.objects.filter(product=c)

                   
                    })
    return HttpResponseRedirect(reverse("dis",args=(listing_id,))) 
@login_required()
def close(request,listing_id,username): 
    if request.method == "POST":
        c = listing.objects.get(pk = listing_id)
        d = c.items.all()
        c.winner = User.objects.get(username=c.bids.money.username)       
        c.save()
        return HttpResponseRedirect(reverse("dis", args = (listing_id,)))

            
def cat(request):
    return render(request,"auctions/index.html",{
        "category":categories.objects.all()
    }) 

def cate(request,category):
    f = categories.objects.get(types = category)

    return render(request, "auctions/index.html",{
        "auction":listing.objects.filter(category = f),
        "shit":category
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
            f = watchlist(users=User.objects.get(username = username))
            f.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
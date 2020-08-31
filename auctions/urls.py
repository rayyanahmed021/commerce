from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("category",views.cat , name = "cat"),
    path("category/<str:category>", views.cate, name="cate"),
    path("listing/<int:listing_id>", views.listings, name = "listings"),
    path("listing/<int:listing_id>/<str:username>", views.watch, name = "watch"),
    path("listing/<int:listing_id>/<str:username>/close", views.close, name = "close"),
    path("listing/<int:listing_id>/<str:username>/comment", views.commy, name = "comment"), 
    path("watchlist/<str:username>", views.watchlists, name = "watchlists"),
    path("create/<str:username>",views.create, name="create")  
]

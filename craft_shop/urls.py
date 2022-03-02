from django.urls import path
from . import views

urlpatterns=[

  path('',views.home, name="home"),
  path('login',views.login, name="login"),
  path('signup',views.signup, name="signup"),
  path('cart',views.cart, name="cart"),
  path('index',views.index, name="index"),
  path('dining',views.dining, name="dining"),
  path('decor',views.decor, name="decor"),
  path('master',views.master, name="master"),
  path('dress',views.dress, name="dress"),
  path('garden',views.garden, name="garden"),
  path('gift',views.gift, name="gift"),
  path('lighting',views.lighting, name="lighting")





]
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('cart', views.cart, name="cart"),
    path('index', views.index, name="index"),
    path('dining', views.dining, name="dining"),
    path('decor', views.decor, name="decor"),
    path('master', views.master, name="master"),
    path('dress', views.dress, name="dress"),
    path('garden', views.garden, name="garden"),
    path('lighting', views.lighting, name="lighting"),
    path('decor_hangingpot', views.decor_hangingpot, name="decor_hangingpot"),
    path('decor_coloredfish', views.decor_coloredfish, name="decor_coloredfish"),
    path('decor_meenakari', views.decor_meenakari, name="decor_meenakari"),
    path('decor_kathakali', views.decor_kathakali, name="decor_kathakali"),
    path('dining_spicebox', views.dining_spicebox, name="dining_spicebox"),
    path('dining_mugs', views.dining_mugs, name="dining_mugs"),
    path('dining_bowls', views.dining_bowls, name="dining_bowls"),
    path('dining_jar', views.dining_jar, name="dining_jar"),
    path('dress_maxidress', views.dress_maxidress, name="dress_maxidress"),
    path('dress_kurtha', views.dress_kurtha, name="dress_kurtha"),
    path('dress_floraldress', views.dress_floraldress, name="dress_floraldress"),
    path('dress_wrapdress', views.dress_wrapdress, name="dress_wrapdress"),
    path('aboutus', views.aboutus, name="aboutus")








]

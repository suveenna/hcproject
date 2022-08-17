from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[

path('custmaster',views.custmaster, name="custmaster"),
path('',views.cust_home, name="cust_home"),
path('cust_decor',views.cust_decor, name="cust_decor"),
path('cust_dining',views.cust_dining, name="cust_dining"),
path('cust_dress', views.cust_dress, name="cust_dress"),
path('cust_garden', views.cust_garden, name="cust_garden"),
path('cust_lighting', views.cust_lighting, name="cust_lighting"),
path('aboutus_cust', views.aboutus_cust, name="aboutus_cust"),
path('cart_cust', views.cart_cust, name="cart_cust"),
path('cust_diningspice', views.cust_diningspice, name="cust_diningspice"),
path('cust_diningmugs', views.cust_diningmugs, name="cust_diningmugs"),
path('myprofile', views.myprofile, name="myprofile"),
path('cust_diningjar', views.cust_diningjar, name="cust_diningjar"),








]

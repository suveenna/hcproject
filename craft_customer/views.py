from django.shortcuts import render

# Create your views here.

def custmaster(request):
    return render(request,'custmaster.html')


def cust_home(request):
    return render(request,'cust_home.html')    

def cust_decor(request):
    return render(request,'cust_decor.html')        

def cust_dining(request):
    return render(request,'cust_dining.html')     

def cust_dress(request):
    return render(request, 'cust_dress.html')


def cust_garden(request):
    return render(request, 'cust_garden.html')


def cust_lighting(request):
    return render(request, 'cust_lighting.html')


def aboutus_cust(request):
    return render(request, 'aboutus_cust.html')    


def cart_cust(request):
    return render(request,'cart_cust.html')       

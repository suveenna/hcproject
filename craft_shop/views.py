from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

     
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def cart(request):
    return render(request,'cart.html')

def index(request):
    return render(request,'index.html')

def dining(request):
    return render(request,'dining.html')

def decor(request):
    return render(request,'decor.html')

def master(request):
    return render(request,'master.html')

def dress(request):
    return render(request,'dress.html')    

def garden(request):
    return render(request,'garden.html')

def gift(request):
    return render(request,'gift.html')

def lighting(request):
    return render(request,'lighting.html')              
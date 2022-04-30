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

def decor_hangingpot(request):
    return render(request,'decor_hangingpot.html')   

def decor_coloredfish(request):
    return render(request,'decor_coloredfish.html')            

def decor_meenakari(request):
    return render(request,'decor_meenakari.html')              

def decor_kathakali(request):
    return render(request,'decor_kathakali.html')         

def dining_spicebox(request):
    return render(request,'dining_spicebox.html')  

def dining_mugs(request):
    return render(request,'dining_mugs.html')    

def dining_bowls(request):
    return render(request,'dining_bowls.html')    

def dining_jar(request):
    return render(request,'dining_jar.html') 

def dress_maxidress(request):
    return render(request,'dress_maxidress.html')  

def dress_kurtha(request):
    return render(request,'dress_kurtha.html')    

def dress_floraldress(request):
    return render(request,'dress_floraldress.html')    

def dress_wrapdress(request):
    return render(request,'dress_wrapdress.html')

def aboutus(request):
    return render(request,'aboutus.html')                                            
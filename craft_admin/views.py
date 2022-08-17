from django.shortcuts import render,redirect

from craft_shop.models import *
# Create your views here.


def admin_home(request):
    cust_data = Customer.objects.all()

    return render(request,'admin_home.html', {'customer': cust_data})  

def delete(self, id):
    print(id)
    Customer.objects.get(id=id).delete()
    return redirect('admin_home')    

    
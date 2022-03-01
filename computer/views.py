from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect
from .models import ComputerBrands
from .models import ComputerSpecification
from .models import Order


def index(request):
    prds = ComputerBrands.get_all_computerbrands()
    # print(products)
    return render(request, 'index.html', {'brands': prds})


# class Index(View):
#     def get(self, request):
#         prds = ComputerBrands.get_all_computerbrands()
#         return render(request, 'index.html', {'brands': prds})
    
def details(request):
    ds=ComputerSpecification.get_all_computerspecifications()
    return render(request,'details.html',{'specdetails':ds})

def form(request):
    if request.method == 'POST':
        postDate = request.POST
        computercode=postDate.get('computercode')
        brandname = postDate.get('brandname')
        quantity = postDate.get('quantity')
        unitrate = postDate.get('unitrate')
        # val1=request.GET['quantity']
        # val2=request.GET['unitrate']
        # res=val1*val2
        # totalprice = res
        totalprice=postDate.get('totalprice')

        order_info = Order(computercode=computercode,brandname=brandname,
                           quantity=quantity,
                           unitrate=unitrate, totalprice=totalprice)
        order_info.register()
        
        return render(request, 'thankyou.html')

    else:
        return render(request, 'form.html')

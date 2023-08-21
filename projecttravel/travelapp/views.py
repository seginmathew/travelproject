from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team




# Create your views here.

def demo(request):
   obj = Place.objects.all()
   team_details = Team.objects.all()
   return render(request, "index.html", {'result': obj, 'details': team_details})



# def addition(request):
#    x=float(request.GET['num1'])
#    y=float(request.GET['num2'])
#    add=x+y
#    sub=x-y
#    product=x*y
#    divide=x/y
#    return render(request,"result.html",{'sum':add,'minus':sub,'multi':product,'div':divide})
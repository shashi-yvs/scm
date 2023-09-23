from django.shortcuts import render
from.models import form
# Create your views here.


def index(request):
   return render(request,"index.html",{"regform":form})

    
      

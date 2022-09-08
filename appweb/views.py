from django.shortcuts import render
from django.http import HttpResponse
#-----------------METHODE D'ACCES A LA PAGE D'ACCUEIL-----------------------------------
def home_view(request):
    #return HttpResponse('Welcome .....')
    return render(request, 'accueil.html')
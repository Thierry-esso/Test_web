from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import capsules
from .serializers import CapsuleSerializer
from .models import Capsules


#-----------------METHODE POUR LISTER TOUS LES CAPSULES---------------------------------
def listeCapsules(request):
    list_capsule = Capsules.objects.all()
    return render(request, 'capsules.html', context = {'list_capsule': list_capsule})

#-----------------METHODE POUR LISTER TOUS LES CAPSULES PAR API--------------------------
@api_view(['GET'])
def allCapsules(request):
    capsules = Capsules.objects.all()
    serialization = CapsuleSerializer(capsules, many=True)
    return Response(serialization.data)

#------------------METHODE POUR VOIR LE DETAIL DE CAPSULE-------------------------------
@api_view(['GET'])
def getCapsule(request, id):
    capsule = Capsules.objects.get(id=id)
    serialization = CapsuleSerializer(capsule)
    return Response(serialization.data)

#---------------------------------METHODE DE CREATION------------------------------------
@api_view(['POST'])
def addCapsule(request):
    serializer = CapsuleSerializer(data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#------------------------------METHODE DE MODIFICATION------------------------------------
@api_view(['PUT'])
def updateCapsule(request, id):
    capsule = Capsules.objects.get(id=id)
    serializer = CapsuleSerializer(instance = capsule, data = request.data, many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#----------------------------- METHODE DE SUPPRESSION------------------------------------
@api_view(['DELETE'])
def deleteCapsule(request, id):
    capsule = Capsules.objects.get(id=id)
    capsule.delete()
    return Response("Capsule supprimé avec succès!!")
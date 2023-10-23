import json
from django.shortcuts import render
from django.http import JsonResponse
from PLAQUES_APP.models import *
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serialiser import Controleserializers, Enregistrementserializers
from rest_framework import generics

# Create your views here.
@api_view(['GET'])
def api_view(request):
    query=Enregistrement.objects.all()
    data={}
    if query:
        data=Controleserializers(query, many=True)
       
    return Response(data.data)

class DetailApiControle(generics.RetrieveAPIView):
    queryset=Enregistrement.objects.all()
    serializer_class=Enregistrementserializers

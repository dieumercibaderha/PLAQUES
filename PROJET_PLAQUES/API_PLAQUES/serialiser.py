from rest_framework import serializers
from PLAQUES_APP.models import *

class Controleserializers(serializers.ModelSerializer):
    class Meta:
        model=Enregistrement
        fields='__all__'

class Enregistrementserializers(serializers.ModelSerializer):
    class Meta:
        model=Enregistrement
        fields='__all__'
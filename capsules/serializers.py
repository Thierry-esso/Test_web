from dataclasses import field
from rest_framework import serializers
from .models import Capsules
class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsules
        #field = '__all__'
        fields = ['id', 'libelle', 'couleur', 'forme', 'description', 'created', 'updated']
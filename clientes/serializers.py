from rest_framework import serializers

from .models import Cliente


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','nombre','apellidos','direccion','ci','telefono',)
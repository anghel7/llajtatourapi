from rest_framework import serializers

from .models import Paquete


class PaqueteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paquete
        fields = ('destino','descripcion','precio','guia','fechaPartida',)
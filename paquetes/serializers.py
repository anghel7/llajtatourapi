from rest_framework import serializers

from .models import Paquete


class PaqueteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paquete
        fields = ('id','destino','descripcion','precio','guia','fechaPartida','img_url')
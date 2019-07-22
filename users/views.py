from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
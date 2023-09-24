from .models import proyectocrud
from rest_framework import viewsets, permissions
from .serializers import projectserializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = proyectocrud.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = projectserializer
from rest_framework import serializers
from .models import proyectocrud

class projectserializer(serializers.ModelSerializer):
    class Meta:
        model = proyectocrud
        fields = ('id', 'fecha_ent', 'observaciones', 'fecha_sal', 'creado')
        read_only_fields = ('creado',)
                
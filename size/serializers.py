from rest_framework import serializers
from .models import Size

class SizeSerializer(serializers.Serializer):
    class Meta:
        model = Size
        fields = '__all__'
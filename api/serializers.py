from rest_framework import serializers
from .models import BukuTamu
class BukuTamuSeliazers(serializers.ModelSerializer):
  class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BukuTamu
        fields = ('__all__')

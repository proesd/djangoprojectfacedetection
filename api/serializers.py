from rest_framework import serializers
from .models import BukuTamu

class FileListSerializer ( serializers.Serializer ) :
    image = serializers.ListField(
                       child=serializers.FileField( max_length=100000,
                                         allow_empty_file=False,
                                         use_url=False )
                                )
    def create(self, validated_data):
        image=validated_data.pop('gambar')
        for img in image:
            image=BukuTamu.objects.create(image=img,nama=nama,**validated_data)
        return image
class BukuTamuSeliazers(serializers.ModelSerializer):
  class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BukuTamu
        fields = ('__all__')

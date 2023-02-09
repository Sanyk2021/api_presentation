from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    model = Album
    fields = '__all__'

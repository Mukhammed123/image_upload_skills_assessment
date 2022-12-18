from rest_framework import serializers
from image_manager.models import Image, PeopleOnImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            "id",
            "url",
            "created_at",
            "user",
        ]

class ImageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = [
            "id",
            "url",
            "location",
            "description",
            "created_at",
            "user",
            "people",
        ]

class PeopleOnImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeopleOnImage
        fields = [
            "name",
        ]
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

class PeopleOnImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PeopleOnImage
        fields = [
            "name",
        ]

class ImageDetailSerializer(serializers.ModelSerializer):
    people = PeopleOnImageSerializer(many=True)
    
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

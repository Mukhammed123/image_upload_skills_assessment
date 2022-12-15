import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from image_manager.models import Image, PeopleOnImage
from image_manager.serializers import ImageSerializer, PeopleOnImageSerializer
from django.core.files.storage import FileSystemStorage
from image_upload_skills_assessment.settings import MEDIA_URL

class ImageView(APIView):

    permission_classes = [IsAuthenticated, ]

    def upload_image(self, file, filename, user_id):
        folder = '{}images/{}'.format(MEDIA_URL, user_id)
        fs = FileSystemStorage(location=folder)
        fln = fs.save(str(user_id) + '/' + filename, file)
        return fs.url(fln)

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def post(self, request):
        user = request.user
        data = request.data
        # try:
        file = data.get("file")
        details = json.loads(data.get("details"))
        description = details.get("description")
        filename = details.get("filename")
        location = details.get("location")
        people = details.get("people")

        url = self.upload_image(file, filename, user.id)

        image = Image.objects.create(url=url, description=description, location=location, user=user)
        people_query_data = [PeopleOnImage(name=str(name), image=image) for name in people]
        bulk_created_list = PeopleOnImage.objects.bulk_create(people_query_data)
        image_serializer = ImageSerializer(image)
        people_serializer = PeopleOnImageSerializer(bulk_created_list, many=True)

        combined_serializer = {
            "image": image_serializer.data,
            "people": people_serializer.data,
        }

        return Response(combined_serializer, status=status.HTTP_201_CREATED)

class ImageDetailView(APIView):
    def get(self, request, pk):
        image = Image.objects.get(id=pk).prefetch_realted("people")

        return Response("Hi")


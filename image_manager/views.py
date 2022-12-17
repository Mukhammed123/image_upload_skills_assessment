import json
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from image_manager.models import Image, PeopleOnImage
from image_manager.serializers import ImageSerializer, PeopleOnImageSerializer
from django.core.files.storage import FileSystemStorage
from backend.settings import MEDIA_URL, STATIC_URL

class ImageView(APIView):

    permission_classes = [IsAuthenticated, ]

    def upload_image(self, file, filename, user_id):
        folder = '{}{}images/{}'.format(STATIC_URL, MEDIA_URL, user_id)
        fs = FileSystemStorage(location=folder)
        fs.save(filename, file)
        return folder + '/' + filename

    def get(self, request):
        params = request.query_params
        images = Image.objects.all()

        location = params.get("location")
        start_date = params.get("start")
        end_date = params.get("end")
        person = params.get("person")

        if location is not None:
            images = images.filter(location__icontains=location)
        if start_date is not None:
            print("==== start date:")
            print(type(start_date))
            images = images.filter(created_at__gte=datetime.fromtimestamp(int(start_date)))
        if end_date is not None:
            print("==== end date:")
            print(datetime.fromtimestamp(int(end_date)))
            images = images.filter(created_at__lte=datetime.fromtimestamp(int(end_date)))
        if person is not None:
            images = images.filter(people__name__icontains=person)

        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        user = request.user
        data = request.data
        try:
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

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ImageDetailView(APIView):
    def get(self, request, pk):
        image = Image.objects.get(id=pk).prefetch_realted("people")

        return Response("Hi")


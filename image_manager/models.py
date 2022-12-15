from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    url = models.URLField()
    location = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PeopleOnImage(models.Model):
    name = models.CharField(max_length=255, default="Anonymous")
    image = models.ForeignKey(Image, related_name="people", on_delete=models.CASCADE)



from django.urls import path
from image_manager.views import ImageView

urlpatterns = [
    path('', ImageView.as_view(), name="image-view")
]
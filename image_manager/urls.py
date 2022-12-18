from django.urls import path
from image_manager.views import ImageView, PeopleOnImageView

urlpatterns = [
    path('people/', PeopleOnImageView.as_view(), name="people-on-image-view"),
    path('', ImageView.as_view(), name="image-view")
]
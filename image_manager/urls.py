from django.urls import path
from image_manager.views import ImageView, PeopleOnImageView, ImageDetailView

urlpatterns = [
    path('people/', PeopleOnImageView.as_view(), name="people-on-image-view"),
    path('image/<str:pk>/', ImageDetailView.as_view(), name='image-deatil-view'),
    path('', ImageView.as_view(), name="image-view")
]
from django.urls import path
from django.db import router
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views

app_name = "rooms"

# router = DefaultRouter()
# router.register("", viewsets.RoomViewset, basename="room")
# urlpatterns = router.urls

urlpatterns = [
    path("", views.RoomsView.as_view()),
    path("search/", views.room_search),
    path("<int:pk>/", views.RoomView.as_view()),
]

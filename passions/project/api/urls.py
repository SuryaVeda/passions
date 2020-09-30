from django.conf.urls import include
from rest_framework import routers
from django.urls import path
from project.api import views
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'muse', views.MusicViewSet)
router.register(r'gymApi', views.GymViewSet)
router.register(r'TravelApi', views.TravelViewSet)
router.register(r'StoriesApi', views.StoriesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
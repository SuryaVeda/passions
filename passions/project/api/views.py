from django.shortcuts import render
from accounts.models import User
from music.models import Youtube
from gym.models import Lessons
from travel.models import Travel
from stories.models import Stories

from rest_framework import viewsets
from project.api.serializers import UserSerializer
from project.api.serializers import MusicSerializer

class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Youtube.objects.all()
    serializer_class = MusicSerializer
class GymViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = MusicSerializer
class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = MusicSerializer
class StoriesViewSet(viewsets.ModelViewSet):
    queryset = Stories.objects.all()
    serializer_class = MusicSerializer        
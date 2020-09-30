from accounts.models import User
from music.models import Youtube
from gym.models import Lessons
from travel.models import Travel
from stories.models import Stories

from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')
class MusicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Youtube
        fields = ('url', 'date', 'name', 'image', 'pdf', 'description', 'url')
class TravelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Travel
        fields = ('url', 'date', 'user', 'name', 'links', 'para1', 'para2','para3','img1','img2','img3')

class GymSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lessons
        fields = ('url', 'date', 'name', 'images', 'img2','img3', 'description', 'url')
class StoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stories
        fields = ('url', 'date', 'name', 'summary', 'image', 'pdf')
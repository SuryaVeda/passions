from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
path('', views.home, name = 'home'),
path('querySearch', views.search, name = 'search'),
path('addNews', views.add_lesson, name = 'add'),
path('editNews/<int:pk>', views.edit_lesson, name = 'edit'),

]
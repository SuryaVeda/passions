from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
path('', views.music, name="main"), 
path('detail/<int:pk>', views.details, name = 'expand' ),
path('edit/<int:pk>', views.edit_lesson, name = 'edit' ),
path('add', views.add_lesson, name="add"), 

]
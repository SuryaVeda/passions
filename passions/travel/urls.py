from django.urls import path
from . import views

app_name = "travel"

urlpatterns = [
path('', views.travel, name="main"),
path('detail/<int:pk>', views.details, name = 'expand' ),
path('edit/<int:pk>', views.edit_lesson, name = 'edit' ),
path('add', views.add_lesson, name="add"),
path('comment/<int:pk>', views.add_comment, name="comment"), 
path('reply/<int:pk>/<int:post_pk>', views.add_reply, name="reply"), 

]
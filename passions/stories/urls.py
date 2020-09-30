from django.urls import path
from . import views

app_name = "stories"

urlpatterns = [
path('', views.stories, name="main"),
path('detail/<int:pk>', views.details, name = 'expand' ),
path('comment/<int:pk>', views.add_comment, name="comment"), 
path('reply/<int:pk>/<int:post_pk>', views.add_reply, name="reply"), 
] 
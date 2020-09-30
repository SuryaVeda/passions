from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
path('signin', views.signin, name = 'login' ),
path('signup/visitor', views.visitor, name='visitor' ),
path('google', views.google_signin, name = 'googleSignin'),
path('signout', views.signout, name = 'logout' ),
]

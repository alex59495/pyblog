from django.urls import path
from blog import views

urlpatterns = [
  path('create_blog', views.create_blog)
]
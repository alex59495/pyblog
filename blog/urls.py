from django.urls import path
from blog import views

urlpatterns = [
  path('create_blog', views.create_blog),
  path('posts', views.post_list, name='home'),
  path('posts/<str:category_name>', views.post_list, name='post_list')
]
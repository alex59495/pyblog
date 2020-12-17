from django.urls import path
from blog import views

urlpatterns = [
  path('create_blog', views.create_blog),
  path('posts', views.post_list, name='home'),
  path('posts/<str:category_name>', views.post_list, name='post_list'),
  path('posts/details/<int:post_id>', views.post_detail, name='post_detail'),
  path('post/detail/<int:post_id>/<str:message>', views.post_detail, name='post_detail_message'),

  path('about', views.about, name='about')
]
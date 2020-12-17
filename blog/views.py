from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from blog.models import Post, Comment
from blog import model_helpers
from blog import navigation
from blog.forms import CommentForm

# Create your views here.
def create_blog(request):
  return HttpResponse('test')

def post_list(request, category_name=model_helpers.post_category_all.slug()):
  category, posts = model_helpers.get_category_and_posts(category_name)
  categories = model_helpers.get_categories()
  
  context = {
    'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
    'category': category,
    'posts': posts,
    'categories': categories
  }

  return render(request, 'list_posts.html', context)

def post_detail(request, post_id, message=''):
  post = get_object_or_404(Post, pk=post_id)
  list_posts = Post.objects.filter(published=True, category__name=post.category.name).exclude(id=post.id)
  comments = post.comments.exclude(status=Comment.STATUS_HIDDEN).order_by('created_at')

  if request.method == "POST":
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment = comment_form.save(commit=False)
      comment.post = post
      comment.save()

      args = [post.pk, 'Your comment has been posted']
      return HttpResponseRedirect(reverse('post_detail_message', args=args) + '#comment')

  else:
    comment_form = CommentForm()

  context = {
    'navigation_items': navigation.navigation_items(navigation.NAV_POSTS),
    'post': post,
    'list_posts': list_posts,
    'comments': comments,
    'comment_form': CommentForm,
    'message': message
  }

  return render(request, 'post_detail.html', context)

def about(request):
  context = {
    'navigation_items': navigation.navigation_items(navigation.NAV_ABOUT),
  }

  return render(request, 'about.html', context)
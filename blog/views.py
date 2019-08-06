''' views.py Docstrings'''

from django.shortcuts import render
from django.utils import timezone
from .models import Post

#from django.contrib.auth.models import User

# Create your views here.


def post_list(request):
    ''' views.py post_list Docstrings'''
    # posts = Post.objects.filter(
    #     published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

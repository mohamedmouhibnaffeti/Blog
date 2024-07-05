from django.shortcuts import render, get_object_or_404

from .models import Post, Comment

def post_list(request):
    post = Post.objects.filter(status='published')

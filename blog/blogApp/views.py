from django.shortcuts import render, get_object_or_404

from .models import Post, Comment

def posts_list(request):
    posts = Post.objects.filter(status='published').order_by('-published_date')
    return render(request, 'blogApp/post_list.html', {'posts': post})

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogApp')
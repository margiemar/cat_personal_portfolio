from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    #blogs = Blog.objects.all()
    blogs = Blog.objects.order_by('-date')[:5]    #5 last posts
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(requiest, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(requiest, 'blog/detail.html', {'blog':blog})
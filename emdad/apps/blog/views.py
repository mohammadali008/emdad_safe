from django.shortcuts import render
from .models import BlogPost

def blog_list_view(request):
    posts = BlogPost.objects.filter(published=True)
    return render(request, 'blog/blog_list.html', {'posts': posts})

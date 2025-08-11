from django.shortcuts import render
from apps.blog.models import BlogPost
from apps.faq.models import FAQ

def homepage_view(request):
    blog_posts = BlogPost.objects.filter(is_active=True).order_by('-created_at')[:3]
    faqs = FAQ.objects.filter(is_active=True)[:3]
    return render(request, 'homepage.html', {
        'blog_posts': blog_posts,
        'faqs': faqs
    })

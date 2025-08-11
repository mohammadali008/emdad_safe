from django.shortcuts import render
from .models import FAQ

def faq_list_view(request):
    faqs = FAQ.objects.filter(is_active=True)
    return render(request, 'faq/faq_list.html', {'faqs': faqs})

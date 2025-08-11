from django.contrib import admin
from django.urls import path, include
from apps.views import homepage_view

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    path("select2/", include("django_select2.urls")),
    # API routes (namespaced)
    path('api/accounts/', include(('apps.accounts.urls', 'accounts'), namespace='accounts_api')),
    path('api/services/', include(('apps.services.urls', 'services'), namespace='services_api')),
    path('api/tickets/', include(('apps.tickets.urls', 'tickets'), namespace='tickets_api')),
    path('api/contact/', include(('apps.contact.urls', 'contact'), namespace='contact_api')),
    path('api/blog/', include(('apps.blog.urls', 'blog'), namespace='blog_api')),
    path('api/faqs/', include(('apps.faq.urls', 'faq'), namespace='faq_api')),

    # Web routes (HTML templates)
    path('', homepage_view, name='homepage'),
    path('blog/', include(('apps.blog.urls', 'blog'), namespace='blog_web')),
    path('faq/', include(('apps.faq.urls', 'faq'), namespace='faq_web')),
    path('contact/', include(('apps.contact.urls', 'contact'), namespace='contact_web')),
    path('services/', include(('apps.services.urls', 'services'), namespace='services_web')),
    path('tickets/', include(('apps.tickets.urls', 'tickets'), namespace='tickets_web')),
    path('accounts/', include(('apps.accounts.urls', 'accounts'), namespace='accounts_web')),
]

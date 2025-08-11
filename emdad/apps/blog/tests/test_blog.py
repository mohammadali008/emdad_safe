
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from blog.models import BlogPost
from django.contrib.auth.models import User

class BlogPostTests(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin', password='admin123')
        self.client.login(username='admin', password='admin123')
        self.blog_data = {
            "title": "Test Blog",
            "slug": "test-blog",
            "content": "This is a test blog post.",
            "tags": ["test", "blog"]
        }
        self.list_url = reverse("blog_api:blog-list")

    def test_create_blog_post_as_admin(self):
        response = self.client.post(self.list_url, self.blog_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_list_blog_posts_as_anonymous(self):
        self.client.logout()
        BlogPost.objects.create(title="T1", slug="t1", content="...", is_active=True)
        BlogPost.objects.create(title="T2", slug="t2", content="...", is_active=False)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_soft_delete_blog_post(self):
        response = self.client.post(self.list_url, self.blog_data, format='json')
        blog_id = response.data['id']
        delete_url = reverse("blog_api:blog-detail", args=[blog_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(BlogPost.objects.get(id=blog_id).is_active)

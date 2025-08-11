from django.db import models
from taggit.managers import TaggableManager

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = TaggableManager()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

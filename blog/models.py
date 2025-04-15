from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.name}"



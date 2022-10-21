import uuid

from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300, unique=True, db_index=True)
    abstract = models.TextField(max_length=500, default='')
    body = models.TextField()
    is_published = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class ColPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    is_article = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

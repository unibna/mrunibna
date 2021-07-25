from random import randint

from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField

from apps.user.models import CustomUser
from django.conf import settings

        
CAT_THUMBNAIL_DEFAULT = 'post/category/default.png'
POST_THUMBNAIL_DEFAULT = 'post/post/default.png'

def post_thumbnail_path(instance, filename):
    return f"{instance.title.replace(' ','_')}/{filename}"


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=64, unique=True, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='post/category/', default=CAT_THUMBNAIL_DEFAULT)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # s = self.name.replace(" ", "-") + randint(0,999999)
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=512)
    thumbnail = models.ImageField(upload_to=post_thumbnail_path, default=POST_THUMBNAIL_DEFAULT)
    content = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # s = self.name.replace(" ", "-") + randint(0,999999)
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
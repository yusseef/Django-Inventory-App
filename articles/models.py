from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank = True, null = True)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(auto_now= False, auto_now_add=False,
     default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

from django.db import models
from django.utils import timezone   
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank = True, null = True)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(auto_now= False, auto_now_add=False,
     default=timezone.now, null=True, blank=True)

    def get_absolute_url(self):
       return reverse('ArticleView',kwargs={'id': self.id})

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        #self.slug = slugify(self.title)
        super().save(*args, **kwargs)

def article_pre_save(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

pre_save.connect(article_pre_save, sender = Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

post_save.connect(article_post_save, sender = Articles)
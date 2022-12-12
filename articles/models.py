from django.db import models
from django.utils import timezone
# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add=True)
    publish = models.DateField(auto_now= False, auto_now_add=False,
     default=timezone.now, null=True, blank=True)

    def __str__(self):
        return self.title
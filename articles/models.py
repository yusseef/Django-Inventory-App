from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title
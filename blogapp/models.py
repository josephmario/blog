from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    is_private = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0}: {1} -> {2}={3}".format(
            self.title,
            self.content,
            self.is_private,
            self.created_at,
            self.updated_at)
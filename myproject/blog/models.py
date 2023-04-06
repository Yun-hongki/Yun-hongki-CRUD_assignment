from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
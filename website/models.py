from django.db import models

# Create your models here.


class blogs(models.Model):
    # Author Name
    author_name = models.CharField(max_length=100)
    # Post
    post = models.TextField()
    # Date
    # Time
    # Tags
    # Img
    img = models.ImageField()
    # Social Media

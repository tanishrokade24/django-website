from django.db import models

# Create your models here.


class blogs(models.Model):
    # Author Name
    name = models.CharField(max_length=20)
    #email = models.EmailField()
    blog = models.TextField()

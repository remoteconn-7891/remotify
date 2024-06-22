from django.db import models

# Create your models here.

class Tree(models.Model):
    firsttreebusiness = models.CharField(max_length=255)
    secondtreebusiness = models.CharField(max_length=255)

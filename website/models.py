from django.db import models

# Create your models here.
from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
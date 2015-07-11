from django.db import models

from spirit.models.category import Category

# Create your models here.

class CustomCategory(Category):
    image = models.ImageField()

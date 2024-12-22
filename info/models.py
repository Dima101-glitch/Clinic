from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sort_number = models.PositiveIntegerField()

    def __str__(self):
        return self.slug

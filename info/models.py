from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sort_number = models.PositiveIntegerField()

    def __str__(self):
        return self.slug


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    directions = models.ManyToManyField(Direction)

    description = models.TextField()

    birth_date = models.DateField()

    experience = models.PositiveIntegerField()
    sort_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.slug} | {self.birth_date}"

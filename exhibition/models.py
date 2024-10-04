from django.contrib.auth.models import User
from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Kitten(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField()
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='kittens'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='kittens'
    )

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    kitten = models.ForeignKey(
        Kitten, on_delete=models.CASCADE,
        related_name='ratings'
    )
    rating = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (
            'user',
            'kitten'
        )

    def __str__(self):
        return f"{self.user.username} оценил {self.kitten.name} на {self.rating}"

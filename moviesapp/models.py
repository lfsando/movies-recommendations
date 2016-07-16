from django.db import models
from django.utils import timezone


class Movie(models.Model):

    title = models.CharField(max_length=200)
    release_date = models.CharField(max_length=9)
    poster = models.ImageField()
    grade = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()

    author = models.ForeignKey('auth.User')
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

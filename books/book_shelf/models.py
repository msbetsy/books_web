from django.db import models


# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = (
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non Fiction'),
    )
    title = models.CharField(max_length=256, null=False)
    author = models.CharField(max_length=256)
    rating = models.FloatField()
    description = models.TextField(null=True)
    reviews = models.IntegerField()
    price = models.FloatField()
    language = models.CharField(max_length=256)
    pages = models.IntegerField()
    year = models.IntegerField()
    genre = models.CharField(max_length=256, choices=GENRE_CHOICES)
    cover = models.ImageField(upload_to="images", blank=True)

    class Meta:
        ordering = ('-year',)

    def __str__(self):
        return self.title

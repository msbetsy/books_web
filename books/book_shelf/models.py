from django.db import models


# Create your models here.
class PublishedManager(models.Manager):
    """Customized manager -> show only published books."""

    def get_queryset(self):
        """Find all books with status published.

        :return: Filtered books.
        :rtype: list
        """
        return super().get_queryset().filter(status='published')


class Book(models.Model):
    """Add books from csv file to Book model."""

    GENRE_CHOICES = (
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non Fiction'),
    )
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
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
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    cover = models.ImageField(upload_to="images", blank=True)
    objects = models.Manager()  # Default manager.
    published = PublishedManager()  # Customized manager.

    class Meta:
        ordering = ('-year',)

    def __str__(self):
        return self.title

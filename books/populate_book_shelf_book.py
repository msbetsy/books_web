"""This module add data to models."""

import csv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_DIR = os.path.join(BASE_DIR, 'bestsellers_with_categories.csv')
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'books.settings')

import django

django.setup()

### ADD BOOKS TO BOOK MODEL###
from book_shelf.models import Book
from faker import Faker
import urllib.request

with open(CSV_DIR, encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    img_number = 0
    for row in reader:
        filename = [str(os.path.join(IMAGE_DIR, 'filename')), str(img_number), ".jpg"]
        imagine = urllib.request.urlretrieve("https://picsum.photos/200/300", ''.join(filename))[0]
        fake = Faker()
        book_genre = ""
        if row[6] == "Non Fiction":
            book_genre = "non_fiction"
        else:
            book_genre = "fiction"
        object = Book.objects.get_or_create(
            title=row[0],
            author=row[1],
            rating=row[2],
            description=fake.text(),
            reviews=row[3],
            price=row[4],
            language=fake.language_name(),
            pages=fake.random_int(100, 1000),
            year=row[5],
            genre=book_genre,
            status='published',
            cover=imagine,
        )[0]
        object.save()
        img_number += 1

"""This module add data to models."""

import csv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CSV_DIR = os.path.join(BASE_DIR, 'populate_models_data/bestsellers_with_categories.csv')
IMAGE_DIR_DB = 'static/book_shelf/images/images_books'
IMAGE_DIR = 'book_shelf/static/book_shelf/images/images_books'

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
        filename = [IMAGE_DIR, '/filename', str(img_number), ".jpg"]
        filename_db = [IMAGE_DIR_DB, '/filename', str(img_number), ".jpg"]
        imagine = urllib.request.urlretrieve("https://picsum.photos/200/300", ''.join(filename))[0]
        imagine_db = ''.join(filename_db)
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
            cover=imagine_db,
        )[0]
        object.save()
        img_number += 1

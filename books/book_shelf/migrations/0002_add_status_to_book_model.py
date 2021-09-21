# Generated by Django 3.2.7 on 2021-09-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('book_shelf', '0001_add_book_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft',
                                   max_length=10),
        ),
    ]

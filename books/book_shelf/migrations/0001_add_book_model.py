# Generated by Django 3.2.7 on 2021-09-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=256)),
                ('rating', models.FloatField()),
                ('description', models.TextField(null=True)),
                ('reviews', models.IntegerField()),
                ('price', models.FloatField()),
                ('language', models.CharField(max_length=256)),
                ('pages', models.IntegerField()),
                ('year', models.IntegerField()),
                ('genre', models.CharField(choices=[('fiction', 'Fiction'), ('non_fiction', 'Non Fiction')], max_length=256)),
                ('cover', models.ImageField(blank=True, upload_to='images')),
            ],
            options={
                'ordering': ('-year',),
            },
        ),
    ]
# Generated by Django 5.1.6 on 2025-02-24 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_book_how_many_days'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='book_title',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='category',
            new_name='category_of_book',
        ),
    ]

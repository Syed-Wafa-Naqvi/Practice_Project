# Generated by Django 5.1.6 on 2025-02-24 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_book_copies_book_is_borrowed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='is_borrowed',
        ),
    ]

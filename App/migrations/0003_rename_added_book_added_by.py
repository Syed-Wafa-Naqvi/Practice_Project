# Generated by Django 5.1.6 on 2025-02-24 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_book_added'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='added',
            new_name='added_by',
        ),
    ]

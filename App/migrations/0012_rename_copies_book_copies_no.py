# Generated by Django 5.1.6 on 2025-02-24 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_alter_book_borrow_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='copies',
            new_name='copies_no',
        ),
    ]

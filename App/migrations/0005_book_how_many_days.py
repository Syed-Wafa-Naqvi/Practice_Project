# Generated by Django 5.1.6 on 2025-02-24 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_rename_added_by_book_borrow_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='How_many_days',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]

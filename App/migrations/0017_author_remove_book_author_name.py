# Generated by Django 5.1.6 on 2025-02-25 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0016_remove_book_copies_book_is_borrowed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='author_name',
        ),
    ]

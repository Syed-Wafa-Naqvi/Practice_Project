# Generated by Django 5.1.6 on 2025-02-26 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0020_rename_is_borrowed_book_want_to_borrow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='want_to_borrow',
            new_name='is_borrowed',
        ),
        migrations.RemoveField(
            model_name='book',
            name='How_many_days',
        ),
        migrations.RemoveField(
            model_name='book',
            name='borrow_date',
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.user')),
            ],
        ),
        migrations.DeleteModel(
            name='BookTransaction',
        ),
    ]

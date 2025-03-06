# Generated by Django 5.1.6 on 2025-03-06 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_remove_billing_price_perday_book_price_perday'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='borrow_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='App.user'),
        ),
        migrations.AlterField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='reserved_books', to='App.user'),
        ),
    ]

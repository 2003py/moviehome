# Generated by Django 4.2.16 on 2024-10-29 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_delete_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image',
            new_name='image_url',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='url',
            new_name='movie_url',
        ),
    ]
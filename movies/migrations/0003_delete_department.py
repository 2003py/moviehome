# Generated by Django 4.2.16 on 2024-09-20 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_department_alter_movie_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
    ]

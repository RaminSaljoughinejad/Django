# Generated by Django 5.0 on 2024-05-12 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_outlet', '0010_language_movie_translated_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='translated_to',
            field=models.ManyToManyField(null=True, to='video_outlet.language'),
        ),
    ]

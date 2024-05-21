# Generated by Django 5.0 on 2024-05-20 20:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='The rating cannot be less than 0!'), django.core.validators.MaxValueValidator(10, message='The rating cannot be More than 10!')]),
        ),
    ]

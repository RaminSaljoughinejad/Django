# Generated by Django 5.0.6 on 2024-05-28 18:06

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'All Tags',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField(auto_now=True)),
                ('image', models.ImageField(null=True, upload_to='posts')),
                ('excerpt', models.CharField(max_length=300)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
            options={
                'verbose_name_plural': 'All Posts',
            },
        ),
    ]

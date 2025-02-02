# Generated by Django 5.0 on 2024-05-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_outlet', '0007_rename_streetstreet_address_street'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.AddField(
            model_name='movie',
            name='translated_to',
            field=models.ManyToManyField(to='video_outlet.language'),
        ),
    ]

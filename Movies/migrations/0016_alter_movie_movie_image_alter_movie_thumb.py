# Generated by Django 4.1.4 on 2023-01-31 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0015_alter_movie_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_image',
            field=models.ImageField(blank=True, null=True, upload_to='movies/images'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumb',
            field=models.FileField(blank=True, null=True, upload_to='movies/images'),
        ),
    ]

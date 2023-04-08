# Generated by Django 4.1.4 on 2023-03-26 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0038_producer_imdb_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvseries',
            name='writers',
            field=models.ManyToManyField(related_name='writers', to='Movies.producer'),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-05 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0030_episode_tv_series_alter_tvseries_cast_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

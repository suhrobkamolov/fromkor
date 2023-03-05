# Generated by Django 4.1.4 on 2023-02-19 17:16

import Movies.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0020_episode_tvseries'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='episode_view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='poster_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tvseries',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to=Movies.models.TVSeries.upload_file_name),
        ),
        migrations.CreateModel(
            name='DailySeriesViews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('views', models.PositiveIntegerField(default=0)),
                ('tv_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.tvseries')),
            ],
        ),
    ]

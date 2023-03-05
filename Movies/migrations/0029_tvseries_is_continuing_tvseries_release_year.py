# Generated by Django 4.1.4 on 2023-02-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0028_rename_name_tvseries_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='tvseries',
            name='is_continuing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tvseries',
            name='release_year',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]

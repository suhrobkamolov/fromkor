# Generated by Django 4.1.4 on 2023-02-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0023_tvseries_imdbid'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='episode',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

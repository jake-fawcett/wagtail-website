# Generated by Django 4.2.13 on 2024-05-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navigationsettings',
            name='mastodon_url',
        ),
        migrations.RemoveField(
            model_name='navigationsettings',
            name='twitter_url',
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='linkedin_url',
            field=models.URLField(blank=True, verbose_name='LinkedIn URL'),
        ),
    ]

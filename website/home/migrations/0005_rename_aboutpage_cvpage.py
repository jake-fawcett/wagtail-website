# Generated by Django 4.2.13 on 2024-05-26 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        ('home', '0004_aboutpage_remove_homepage_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutPage',
            new_name='CvPage',
        ),
    ]
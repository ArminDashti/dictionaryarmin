# Generated by Django 4.0.4 on 2022-06-01 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_en_words'),
    ]

    operations = [
        migrations.DeleteModel(
            name='en_words',
        ),
    ]
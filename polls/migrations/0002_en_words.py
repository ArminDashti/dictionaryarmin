# Generated by Django 4.0.4 on 2022-05-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='en_words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words', models.CharField(max_length=200)),
                ('defn', models.CharField(max_length=200)),
            ],
        ),
    ]

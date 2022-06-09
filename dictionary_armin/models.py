from django.db import models

class words(models.Model):
    # id = models.IntegerField(primary_key=True, auto_now_add=True)
    english_word = models.CharField(max_length=100)
    persian_meaning = models.CharField(max_length=100, default='-')
    english_meaning = models.CharField(max_length=100)
    search_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

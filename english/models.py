from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    en_word = models.CharField(max_length=200)
    defn = models.CharField(max_length=200)

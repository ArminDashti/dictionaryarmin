from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, HttpResponse

class words(models.Model):
    word = models.CharField(max_length=100)
    defn = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        if self.word == "tesla":
            self.word = 'tesla is good'
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


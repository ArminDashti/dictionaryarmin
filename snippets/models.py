from django.db import models

class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE) #owner_id in database table
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    code = models.TextField()
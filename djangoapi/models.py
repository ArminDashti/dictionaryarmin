from django.db import models
from django.contrib.auth.models import User

class words(models.Model):
    word = models.CharField(max_length=100)
    defn = models.CharField(max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippetsv', on_delete=models.CASCADE, null=True)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    # class Meta:
    #     ordering = ['created']
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




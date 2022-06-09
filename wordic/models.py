from django.db import models

class dict(models.Model):
    en_word = models.CharField(max_length=100)
    defn_word = models.CharField(max_length=100, verbose_name="te")
    type_word = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if self.en_word == "tesla":
            self.en_word = 'tesla is good'
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
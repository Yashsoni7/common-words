from django.db import models

class common_word(models.Model):
    word = models.CharField(max_length=100)
    freq = models.IntegerField()
    url = models.CharField(max_length=500)
    
    def __str__(self):
        return self.url
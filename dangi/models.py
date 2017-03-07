from django.db import models


# Create your models here.

class Vocabulary(models.Model):
    day = models.PositiveIntegerField()
    word = models.CharField(max_length=40)
    definition = models.CharField(max_length=40)

    def __str__(self):
        return str(self.day) + " / " + self.word

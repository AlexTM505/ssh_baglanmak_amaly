from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
        
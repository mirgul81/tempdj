from django.db import models

class Regions(models.Model):
    name = models.CharField(max_length=60)
    info = models.TextField()

    def __str__(self):
        return self.name


class Areas(models.Model):
    name = models.CharField(max_length=60)
    info = models.TextField()

    def __str__(self):
        return self.name
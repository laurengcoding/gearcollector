from django.db import models

class Gear(models.Model):
    brand = models.CharField(max_length=256)
    make = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    colour = models.CharField(max_length=256)

    def __str__(self):
        return self.type
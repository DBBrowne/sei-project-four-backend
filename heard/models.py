from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
class HeardEvent(models.Model):
    title = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100, blank=True)
    location_lat = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)])
    location_long = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)])
    start = models.DateTimeField()
    finish = models.DateTimeField()
    image = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.title}'


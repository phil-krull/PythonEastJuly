from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=55)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # grapes_that_belongs_to hidden key that references the related name in Grape class
    # produced_by hidden key that references the related name in Producer class
    # objects object
    def __str__(self):
        return f'<Region object: Name={self.name}, Latitude={self.latitude}, Longitude={self.longitude}>'

class Grape(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    region = models.ForeignKey(Region, related_name='grapes_that_belongs_to', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'<Grape object: Name={self.name}, description={self.description}>'

class Producer(models.Model):
    name = models.CharField(max_length=55)
    regions = models.ManyToManyField(Region, related_name='produced_by')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
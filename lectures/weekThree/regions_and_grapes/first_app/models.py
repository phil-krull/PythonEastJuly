from django.db import models

class RegionManager(models.Manager):
    # refferencing the objects object inside the Region class
    def validate_region(self, region_data_from_view):
        print('region data in model',region_data_from_view)
        is_valid = True
        error_messages = []
        if len(region_data_from_view['form_name']) < 1:
            is_valid = False
            error_messages.append('Region name is required!')
        if len(region_data_from_view['form_latitude']) < 1:
            is_valid = False
            error_messages.append('Region latitude is required!')
        if len(region_data_from_view['form_longitude']) < 1:
            is_valid = False
            error_messages.append('Region longitude is required!')
        if int(region_data_from_view['form_latitude']) > 999 or int(region_data_from_view['form_longitude']) > 999:
            is_valid = False
            error_messages.append('Latidute or Longitude is in valid')
        return {
            'status': is_valid,
            'messages': error_messages
        }

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=55)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = RegionManager()

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
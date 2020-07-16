from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=55)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # objects object
    def __str__(self):
        return f'<Region object: Name={self.name}, Latitude={self.latitude}, Longitude={self.longitude}'

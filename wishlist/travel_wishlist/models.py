from django.db import models
from django.utils import timezone

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length = 200)
    visited = models.BooleanField(default=False)
    date = models.DateField(blank = True, null = True)
    notes = models.CharField(max_length = 1000, blank = True, null = True)


    def __str__(self):
        return '%s visited? %s'% (self.name, self.visited)

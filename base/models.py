from django.db import models

# Create your models here.

class Room(models.Model):
    # host =
    # topic =
    name = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    # participants = 
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

def __str__(self): # __str__ special py method (dunder-double underscored)to convert generic object identifier to human readable string representation
    return self.name
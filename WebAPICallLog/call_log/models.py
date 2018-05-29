from django.db import models
from datetime import datetime 

TYPE = (
    ('S', "Start"),
    ('E', "End")
)

# Create your models here.
class Call(models.Model):
    id = models.AutoField(primary_key = True)
    typeCall = models.CharField(choices=TYPE, default='S', max_length=10)
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)
    call_id = models.IntegerField(default=0)
    source = models.CharField(max_length=20, blank=True)
    destination = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ('id',)

class CallRecord(models.Model):
    id = models.AutoField(primary_key = True)
    source = models.CharField(max_length=20, blank=True)
    destination = models.CharField(max_length=20, blank=True)
    start_time = models.DateTimeField(default=None, blank=True, null=True)
    end_time = models.DateTimeField(default=None, blank=True, null=True)
    duration = models.TimeField(default=None, blank=True, null=True)
    price = models.DecimalField(default=None, blank=True, null=True, max_digits=5, decimal_places=2)

    class Meta:
        ordering = ('id',)

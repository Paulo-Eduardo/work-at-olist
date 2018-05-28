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
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)

    class Meta:
        ordering = ('id',)
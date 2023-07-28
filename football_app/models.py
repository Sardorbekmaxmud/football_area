from datetime import datetime

from django.db import models
from user.models import CustomUser

# Create your models here.


class StadiumModel(models.Model):
    name = models.CharField(max_length=120, default='')
    address = models.TextField(default='')
    contact = models.CharField(max_length=13, default='')
    images = models.ImageField(upload_to='Images/',blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stadium'

class BronModel(models.Model):
    stadium = models.ForeignKey(StadiumModel,on_delete=models.CASCADE,default=None,null=True)
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,default=None,null=True)
    started_at = models.DateTimeField(default=datetime.now)
    end_at = models.DateTimeField(default=datetime.now)
    price = models.IntegerField(default=0)
    bron_status = models.BooleanField(default=False,null=True)

    def __str__(self):
        return f"{self.user} {self.stadium.name}"

    class Meta:
        db_table = 'bron'

from datetime import datetime

from django.db import models
from user.models import CustomUser

# Create your models here.


class StadiumModel(models.Model):
    name = models.CharField(max_length=120, default='')
    address = models.TextField()
    contact = models.CharField(max_length=13, default='')
    images = models.ImageField(upload_to='Images/')
    price = models.IntegerField(default=0)
    started_at = models.DateTimeField(default=datetime.now)
    end_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(CustomUser,on_delete=models.SET_NULL,default=None,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'stadium'

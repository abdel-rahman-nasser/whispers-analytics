from email.policy import default
from django.db import models
from picklefield.fields import PickledObjectField

class Query_Data(models.Model):
    k = models.CharField(max_length=200)
    analysis = models.CharField(max_length=200)
    lim = models.IntegerField(default=0)
    lang=models.CharField(max_length=10,default="en")
    df_info = PickledObjectField()




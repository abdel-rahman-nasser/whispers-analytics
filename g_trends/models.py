from django.db import models
from picklefield.fields import PickledObjectField

class Data_Save(models.Model):
    trend = models.CharField(max_length=30)
    df = PickledObjectField()
    time_df = PickledObjectField()
    rltd_dict = PickledObjectField()

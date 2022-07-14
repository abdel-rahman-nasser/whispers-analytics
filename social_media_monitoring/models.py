from django.db import models
from picklefield.fields import PickledObjectField


class social_Data(models.Model):
    s_user = models.CharField(max_length=200)
    insta = models.CharField(max_length=200)
    face_url = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
   

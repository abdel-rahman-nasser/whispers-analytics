from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.


class Chatbot_Model(models.Model):
    name = models.CharField(max_length=200, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    intents = JSONField(default=dict,null=False,)

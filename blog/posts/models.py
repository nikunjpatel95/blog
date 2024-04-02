from django.db import models
from datetime import datetime

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100000000)
    created_date=models.DateTimeField(default=datetime.now, blank=True)
from django.db import models

class LongToShort(models.Model):
    longurl=models.URLField(max_length=255)
    shorturl=models.CharField(max_length=50,unique=True)
    date=models.DateField(auto_now_add=True)
    clicks=models.IntegerField(default=0)

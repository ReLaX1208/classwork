from django.db import models

class Bb(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    publish = models.DateTimeField(auto_now_add=True, db_index=True)
from django.db import models

class Sales(models.Model):
    order_id = models.IntegerField()
    product = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    date = models.DateField()
    total_amount = models.FloatField()
from django.db import models


class DeChiro(models.Model):
'''
This model describes the database setup for the Chiro. Perhaps we should make a separate table
for including the colours. Also the model(types) is open for discussion
'''
    product_name = models.CharField(max_length=200)
    # color = (refference to the colours table below)
    quantity = models.IntegerField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # pub_date = models.DateTimeField('date published')

class Colour(models.Model):
'''
This model describes the database setup for the colours for the chiros
'''
    colour = models.CharField(max_length=200)

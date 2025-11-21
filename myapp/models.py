from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
     return self.Item_name
    
    Item_name = models.CharField(max_length=50)
    Item_desc = models.CharField(max_length=255)
    Item_price = models.IntegerField()


    
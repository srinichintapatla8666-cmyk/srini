from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):

    def __str__(self):
     return self.Item_name

    def get_absolute_url(self):
        return reverse('myapp:index')

    user_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)    
    Item_name = models.CharField(max_length=50)
    Item_desc = models.CharField(max_length=255)
    Item_price = models.IntegerField()
    Item_image = models.CharField(max_length=500, default="https://imgcdn.stablediffusionweb.com/2024/10/14/b4676dd8-6fef-4df9-9a4c-5d1c72155b40.jpg")
    


    
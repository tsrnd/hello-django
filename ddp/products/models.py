from django.db import models

# Create your models here.
class Products(models.Model):
    # song title
    name_product = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    price = models.IntegerField(null=False)

    def __str__(self):
        return "{} - {}".format(self.name_product, self.price)  

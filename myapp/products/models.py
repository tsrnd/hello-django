from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    category = models.SmallIntegerField(null=False)
    im_url = models.CharField(max_length=255)

    def __str__(self):
        return "{} = {}".format(self.name, self.category)

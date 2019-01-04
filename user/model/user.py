from django.db import models



class User(models.Model):
    name = models.CharField(max_length = 255, null = False)

    def __str__(self):
        return "%s"%self.name

    class Meta:
        db_table = "User"

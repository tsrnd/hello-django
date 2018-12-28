from django.db import models

# Create your models here.
class Topic(models.Model):
    content = models.TextField(db_column='content', max_length=50, blank=False, null=False)

    class Meta:
        managed = False
        #Table name
        db_table = 'tbl_topics'
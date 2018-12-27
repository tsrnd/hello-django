from django.db import models

# Create your models here.
class Topic(models.Model):
    topicId = models.IntegerField(db_column='topic_id', null=False)
    textValue = models.TextField(db_column='topic_content', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.textValue[:50]

    class Meta:
        # managed = False
        #Table name
        db_table = 'tbl_topics'
        #for events.
        #ordering = ('created',)
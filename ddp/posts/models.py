from django.db import models
from topics.models import Topic


class Post(models.Model):
    postId = models.IntegerField(db_column='post_id', null=False)
    textValue = models.TextField(db_column='post_content', max_length=50, blank=False, null=False)
    topic = models.ForeignKey('topics.Topic', related_name='posts', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.textValue[:50]

    class Meta:
        # managed = False
        #Table name
        db_table = 'tbl_posts'
        #for events.
        #ordering = ('created',)

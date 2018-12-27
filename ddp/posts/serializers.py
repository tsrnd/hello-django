from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.ReadOnlyField(source='topic.topicId')
 
    class Meta:
        model = Post
        fields = ('id', 'text', 'topic')
        extra_kwargs = {
            'url': {
                'view_name': 'post:post-detail',
            }
        }

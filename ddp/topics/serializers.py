from rest_framework import serializers

from .models import Topic


class TopicSerializer(serializers.HyperlinkedModelSerializer): 

    def create(self, validated_data):
        topic = Topic(content = validated_data.get('content', None))
        topic.save()
        return topic
    
    def update(self, instance, validated_data):
        for field in validated_data:
            if field!= 'id':
                instance.__setattr__(field, validated_data.get(field))
        instance.save
        return instance

    class Meta:
        model = Topic
        fields = ('id', 'content')
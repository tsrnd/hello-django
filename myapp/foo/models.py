from django.db import models
from rest_framework import serializers


class Foo(models.Model):
    def info(self):
        print('Foo')


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class QuestionSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(max_length=5)
    pub_date = serializers.DateField()

    class Meta:
        model = Question
        fields = "__all__"
    
    def create(self, params):
        return Question.objects.create(**params)

    def update(self, instance, data):
        instance.question_text = data.get('question_text', instance.question_text)
        instance.pub_date = data.get('pub_date', instance.pub_date)
        instance.save()
        return instance

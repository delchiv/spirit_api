
from rest_framework import serializers

from spirit.models.category import Category
from spirit.models.topic import Topic


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic

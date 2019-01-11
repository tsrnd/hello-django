from rest_framework import serializers
from .models import Post


# Định nghĩa model cần serialize và các trường:
class PostListSerializer(serializers.ModelSerializer):
    created_formated = serializers.SerializerMethodField(read_only=True)

    def get_created_formated(self, post):
        # return dd-mm-yyyy format
        return post.created.strftime("%d-%m-%Y")

    class Meta:
        model = Post
        # ko dùng đến updated và created
        fields = ('id', 'title', 'content', 'draft', 'read_time',
                  'created_formated')
        # định nghĩa trường chỉ cho phép đọc
        read_only_fields = ('draft', 'read_time')

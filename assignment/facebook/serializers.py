
from rest_framework import serializers
from .models import User, Post, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class ValidateUserSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    id_number = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"


class ValidatePostSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"


class ValidateCommentSerializer(serializers.Serializer):
    about_comment = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"





# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#
#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.save()
#         return instance
#
#
#
# class SnippetSerializer1(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos']


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

#
# class ValidateUserSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True)
#     id_number = serializers.IntegerField(required=True)
#
#     class Meta:
#         fields = ["name", "id_number"]

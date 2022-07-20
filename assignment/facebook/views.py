from django.http import HttpResponse
from rest_framework import viewsets

from .models import Post, User, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class PostViewSet(viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import PostSerializer

        serial_obj = PostSerializer(data={"name": kwargs["name"],
                                          "description": kwargs["description"],
                                          "user": kwargs["user_id"]})
        if serial_obj.is_valid(raise_exception=True):
            post = serial_obj.save()
            return HttpResponse(post)


    def list(self, request, *args, **kwargs):
        from .serializers import PostSerializer
        from .models import Post

        post_obj = Post.objects.all()
        serial_obj = PostSerializer(post_obj, many=True)
        response = serial_obj.data
        return HttpResponse(response)

    def update(self, request, *args, **kwargs):
        from .serializers import PostSerializer
        from .models import Post

        post_obj = Post.objects.get(id=kwargs["user_id"])
        post_obj.description = kwargs["description"]
        post_obj.save()
        return HttpResponse(post_obj.description)

    def destroy(self, request, *args, **kwargs):
        from .serializers import PostSerializer
        from .models import Post

        post_obj = Post.objects.get(id=kwargs["user_id"])
        response = post_obj.delete()
        return HttpResponse(response)


class CommentViewSet(viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CommentSerializer, ValidateCommentSerializer

        validate = ValidateCommentSerializer(data={"about_comment": kwargs["about_comment"]})
        if validate.is_valid(raise_exception=True):
            serializer_obj = CommentSerializer(data={"about_comment": kwargs["about_comment"],
                                                     "post": kwargs["post_id"],
                                                     "user": kwargs["user_id"]})
            if serializer_obj.is_valid(raise_exception=True):
                comment = serializer_obj.save()
                return HttpResponse(comment.about_comment)

    def update(self, request, *args, **kwargs):
        from .serializers import CommentSerializer, ValidateCommentSerializer
        from .models import Comment

        comment_obj = Comment.objects.get(id=kwargs["comment_id"])
        comment_obj.about_comment = kwargs["text"]
        comment_obj.save()

        return HttpResponse(comment_obj.about_comment)

    def list(self, request, *args, **kwargs):
        from .serializers import CommentSerializer, ValidateCommentSerializer
        from .models import Comment

        comment_obj = Comment.objects.all()
        serializer_obj = CommentSerializer(comment_obj, many=True)
        response = serializer_obj.data
        return HttpResponse(response)

    def destroy(self, request, *args, **kwargs):
        from .serializers import CommentSerializer, ValidateCommentSerializer
        from .models import Comment

        comment_obj = Comment.objects.get(id=kwargs["comment_id"])
        response = comment_obj.delete()
        return HttpResponse(response)


# class UserViewSet(viewsets.GenericViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def list(self, request, *args, **kwargs):
#         return HttpResponse("GET METHOD CALLED")
#
#     def create(self, request, *args, **kwargs):
#         from .serializers import UserSerializer, ValidateUserSerializer
#
#         validate = ValidateUserSerializer(data={"name": kwargs["name"], "id_number" : kwargs["id_number"]})
#         if validate.is_valid(raise_exception=True):
#             serializer_obj = UserSerializer(data={"name": kwargs["name"], "id_number": kwargs["id_number"]})
#             if serializer_obj.is_valid(raise_exception=True):
#                 serializer_obj.save()
#         return HttpResponse(serializer_obj)
#





#
#
# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
#
# class UserViewSet(viewsets.GenericViewSet):
#     queryset = Post.objects.all()
#     serializer_class = UserSerializer
#
#     def list(self, request, *args, **kwargs):
#         return HttpResponse("GET METHOD CALLED")
#
#     def create(self, request, *args, **kwargs):
#         from .serializers import CreateUserSerializer, ValidateUserSerializer
#
#         validate = ValidateUserSerializer(data={"name": kwargs["name"], "id_number": kwargs["id_number"]})
#         if validate.is_valid(raise_exception=True):
#             serializer_obj = CreateUserSerializer(data={"name": kwargs["name"], "id_number": kwargs["id_number"]})
#             if serializer_obj.is_valid(raise_exception=True):
#                 serializer_obj.save()
#
#         return HttpResponse("POST METHOD CALLED")
#
#     def update(self, request, *args, **kwargs):
#         return HttpResponse("PUT METHOD CALLED")
#
#     def destroy(self, request, *args, **kwargs):
#         return HttpResponse("DELETE METHOD CALLED")
#
#
#
#

#
# def create_user(request, name, id_number):
#     user_obj = User.objects.create(name=name, id_number=id_number)
#     return HttpResponse(user_obj)
#
#
# def create_post(request,  user_id, name, description):
#     post_obj = Post.objects.create(user_id=user_id, name=name, description=description)
#     return HttpResponse(post_obj)
#
#
# def create_comment(request, user_id, post_id, about_comment):
#     comment_obj = Comment.objects.create(user_id=user_id, post_id = post_id, about_comment=about_comment)
#     return HttpResponse(comment_obj)
#
#

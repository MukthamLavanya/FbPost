from django.http import HttpResponse
from rest_framework import viewsets

from .models import Post, User, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer



class CommentViewSet(viewsets.GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


    def create(self, request, *args, **kwargs):
        name = kwargs["name"]
        from .serializers import CommentSerializer, ValidateCommentSerializer

        validate = ValidateCommentSerializer(data={"about_comment": name})
        if validate.is_valid(raise_exception=True):
            serializer_obj = CommentSerializer(data={"about_comment": name})
            if serializer_obj.is_valid(raise_exception=True):
                comment = serializer_obj.save()
                ser_obj = CommentSerializer(comment)
                return HttpResponse(ser_obj.data)


    def update(self, request, *args, **kwargs):
        from .serializers_practice import update_comment

        response = update_comment(about_comment="Nice", id=11)
        return HttpResponse(response)


    def get(self, request, *args, **kwargs):
        from .serializers_practice import get_comment

        response = get_comment()
        return HttpResponse(response)

    def destroy(self, request, *args, **kwargs):
        from .serializers_practice import destroy_comment

        response = destroy_comment()
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

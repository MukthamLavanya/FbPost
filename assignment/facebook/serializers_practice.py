def create_user(name, id_number):
    from .serializers import UserSerializer, ValidateUserSerializer

    validate = ValidateUserSerializer(data={"name": "name", "id_number": "id_number"})
    if validate.is_valid(raise_exception=True):
        serializer_obj = UserSerializer(data={"name": "name", "id_number": "id_number"})
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.save()


create_user(name="Bujji", id_number=134, id=17)


def create_comment(about_comment):
    from .serializers import CommentSerializer, ValidateCommentSerializer

    validate = ValidateCommentSerializer(data={"about_comment": "about_comment"})
    if validate.is_valid(raise_exception=True):
        serializer_obj = CommentSerializer(data={"about_comment": "about_comment"})
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.save()


create_comment(about_comment="Great")


def update_comment(about_comment):
    from .serializers import CommentSerializer, ValidateCommentSerializer
    from .models import Comment

    comment_obj = Comment.objects.get(id=id)
    validate = ValidateCommentSerializer(data={"about_comment": "about_comment"})
    if validate.is_valid(raise_exception=True):
        serializer_obj = CommentSerializer(data={"about_comment": "about_comment"}, instance=comment_obj)
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.save()


update_comment(about_comment="Nice", id=11)


def get_comment():
    from .serializers import CommentSerializer, ValidateCommentSerializer
    from .models import Comment

    comment_obj = Comment.objects.all
    validate = ValidateCommentSerializer(data={"about_comment": "about_comment"})
    if validate.is_valid(raise_exception=True):
        serializer_obj = CommentSerializer(comment_obj, many=True)
        if serializer_obj.is_valid(raise_exception=True):
            return serializer_obj.data


output = get_comment()
print(output)


def destroy_comment(id):
    from .serializers import CommentSerializer, ValidateCommentSerializer
    from .models import Comment

    comment_obj = Comment.objects.get(id=id)
    validate = ValidateCommentSerializer(data={"about_comment": "about_comment"})
    if validate.is_valid(raise_exception=True):
        serializer_obj = CommentSerializer(data={"about_comment": "about_comment"}, instance=comment_obj)
        if serializer_obj.is_valid(raise_exception=True):
            serializer_obj.delete()


destroy_comment(id=15)



# def create_user(user_name, id_number):
#     from .serializers import CreateUserSerializer
#
#     serializer_obj = CreateUserSerializer(data={"name": user_name, "id_number": id_number})
#     if serializer_obj.is_valid(raise_exception=False):
#         serializer_obj.save()
#
#
# create_user(user_name="ADILAKSHMI", id_number=12312321)


# def update_user(id, user_name, id_number):
#     from .serializers import CreateUserSerializer
#     from .models import User
#
#     user_obj = User.objects.get(id=id)
#     serializer_obj = CreateUserSerializer(
#         data={"name": user_name, "id_number": id_number},
#         instance=user_obj)
#     if serializer_obj.is_valid(raise_exception=True):
#         serializer_obj.save()
#
#
# update_user(user_name="Lavanya", id_number=9999999, id=13)


# def get_users():
#     from .serializers import CreateUserSerializer
#     from .models import User
#
#     users = User.objects.all()
#     serializer_obj = CreateUserSerializer(users, many=True)
#     return serializer_obj.data
#
#
# response = get_users()
# print(response)

#
# def create_user(user_name, id_number):
#     from .serializers import CreateUserSerializer, ValidateUserSerializer
#
#     validate = ValidateUserSerializer(data={"name": user_name})
#     if validate.is_valid(raise_exception=True):
#         serializer_obj = CreateUserSerializer(data={"name": user_name, "id_number": id_number})
#         if serializer_obj.is_valid(raise_exception=True):
#             serializer_obj.save()
#
#
# create_user(user_name="ADILAKSHMI", id_number='')
#

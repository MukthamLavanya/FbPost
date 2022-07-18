# from django.db import models
#
#
# class User(models.Model):
#     name = models.CharField(max_length=200)
#     id_number = models.IntegerField()
#
#
# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     description = models.CharField(max_length=500)
#
#
# class Snippet(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100, blank=True, default='')
#     code = models.TextField()
#     linenos = models.BooleanField(default=False)
#
#     class Meta:
#         ordering = ['created']
#
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    id_number = models.IntegerField()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    about_comment = models.CharField(max_length=500)


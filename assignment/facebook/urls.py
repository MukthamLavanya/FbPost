from django.urls import path

from . import views
from .views import  CommentViewSet, PostViewSet

urlpatterns = [
    path('<str:name>/<str:description>/<int:user_id>/', views.PostViewSet.as_view(
        {'post': 'create'}), name="create_post"),
    path('getpost/', views.PostViewSet.as_view(
        {'get': 'list'}), name="get_post"),
    path('<int:user_id>/<str:description>/postupdate/', views.PostViewSet.as_view(
        {'put': 'update'}), name="update_post"),
    path('<int:user_id>/', views.PostViewSet.as_view(
        {'delete': 'destroy'}), name="delete_post"),
    path('<str:about_comment>/<int:post_id>/<int:user_id>/', views.CommentViewSet.as_view(
        {'post': 'create'}), name="comment"),
    path('<int:comment_id>/<str:text>/comments/', views.CommentViewSet.as_view(
        {'put': 'update'}), name="update_comment"),
    path('getcomment/', views.CommentViewSet.as_view(
        {'get': 'list'}), name="get_comment"),
    path('<int:comment_id>/', views.CommentViewSet.as_view(
        {'delete': 'destroy'}), name="delete_comment"),
    #path('<str:name>/<int:id_number>/', views.create_user, name="user"),
    #path('<int:user_id>/<str:name>/<str:description>/', views.create_post, name="post"),
    #path('<int:user_id>/<int:post_id>/<str:about_comment', views.create_comment, name="comment"),
    # path('<str:name>/<str:post_name>/<str:about_post>/user/', views.user, name="user"),
    # path('<str:name>/', views.create_user, name="username"),
    # path('<str:name>/<str:post_name>/<str:about_post>/user_post/', views.user_post, name="user_post"),
    # path('<int:user_id>/userid/', views.get_user_id, name="userid"),
    # path('<int:user_id>/deleteid/', views.delete_user_id, name="deleteid")
    # path('/', views.snippet_list, name="snippet_list"),
    # path('<int:pk>/', views.snippet_detail, name="snippet_detail"),
    # path('<int:user_id>/', PostViewSet.as_view({'get': 'list'}), name="name"),
    # path('<str:name>/', UserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name="username"),
    # path('<str:name>/', views.UserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name="username"),

]
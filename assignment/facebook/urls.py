from django.urls import path

from . import views
from .views import  CommentViewSet

urlpatterns = [
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
    path('<str:name>/', views.UserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}), name="username"),

]
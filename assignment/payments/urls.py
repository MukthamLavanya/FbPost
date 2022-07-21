from django.urls import path
from . import views


urlpatterns = [
    path('<str:name>/<int:age>/<int:date_of_birth>/<str:qualification>/<str:place>/user_details/',
         views.UserDetailsViewSet.as_view({'post': 'create'}), name="user_details"),
    path('<str:name>/<int:fees>/course_details/',
         views.CourseDetailsViewSet.as_view({'post': 'create'}), name="course_details"),
    path('<int:user_id>/<int:course_id>/<str:name>/<int:fees>/register_details/',
         views.RegisterCourseDetailViewSet.as_view({'post': 'create'}), name="register_details"),
    path('<int:user_id>/<int:course_id>/<int:amount_paid>/payment_details/',
         views.CreatePaymentDetailsViewSet.as_view({'post': 'create'}), name="payment_details"),

    path('<str:name>/<int:age>/<int:date_of_birth>/<str:qualification>/<str:place>/user',
         views.UserViewSet.as_view({'post': 'create'}), name="create_user"),
    path('<str:name>/<int:fees>/course/', views.CourseViewSet.as_view({'post': 'create'}), name="create_course"),
    path('<int:user_id>/<int:course_id>/<str:name>/<int:fees>/register/',
         views.RegisterCourseViewSet.as_view({'post': 'create'}), name="register_course"),
    path('<int:user_id>/<int:course_id>/<int:amount_paid>/payment/',
         views.CreatePaymentViewSet.as_view({'post': 'create'}), name="create_payment"),
    path('users/', views.GetUserViewSet.as_view({'get': 'list'}), name="get_users"),
    path('courses/', views.GetCourseViewSet.as_view({'get': 'list'}), name="get_courses"),
    path('course_user/', views.GetUserCoursesViewSet.as_view({'get': 'list'}), name="get_user_course"),
    path('course_payment/', views.GetCoursePaymentViewSet.as_view({'get': 'list'}), name="get_course_payment"),
    path('<int:user_id>/course_details/', views.GetUserCourseViewSet.as_view({'get': 'list'}), name="get_user_courses"),
    path('<int:user_id>/get_payment/', views.GetUserCoursePayments.as_view({'get': 'list'}),
         name="get_user_course_payment")
]

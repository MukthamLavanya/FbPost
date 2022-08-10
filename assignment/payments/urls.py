from django.urls import path
from . import views


urlpatterns = [
    path('<str:name>/<int:age>/<int:date_of_birth>/<str:qualification>/<str:place>/user_details/',
         views.UserDetailsViewSet.as_view({'post': 'create'}), name="user_details"),
    path('<str:name>/<int:fees>/course_details/',
         views.CourseDetailsViewSet.as_view({'post': 'create'}), name="course_details"),
    path('<int:user_id>/<int:course_id>/register/',
         views.RegisterCourseDetailViewSet.as_view({'post': 'create'}), name="register"),
    path('<int:user_id>/<int:course_id>/<int:amount_paid>/payment_details/',
         views.CreatePaymentDetailsViewSet.as_view({'post': 'create'}), name="payment_details"),

    path('<str:name>/<int:age>/<int:date_of_birth>/<str:qualification>/<str:place>/user/',
         views.UserViewSet.as_view({'post': 'create'}), name="create_user"),
    path('<str:name>/<int:fees>/course/', views.CourseViewSet.as_view({'post': 'create'}), name="create_course"),
    path('<int:user_id>/<int:course_id>/registers/',
         views.RegisterCourseViewSet.as_view({'post': 'create'}), name="register"),
    path('<int:user_id>/<int:course_id>/<int:amount_paid>/payment/',
         views.CreatePaymentViewSet.as_view({'post': 'create'}), name="create_payment"),
    path('users/', views.GetUserViewSet.as_view({'get': 'list'}), name="get_users"),
    path('courses/', views.GetCourseViewSet.as_view({'get': 'list'}), name="get_courses"),
    path('course_user/', views.GetUserCoursesViewSet.as_view({'get': 'list'}), name="get_user_course"),
    path('course_payment/', views.GetCoursePaymentViewSet.as_view({'get': 'list'}), name="get_course_payment"),
    path('<int:user_id>/course_details/', views.GetUserCourseViewSet.as_view({'get': 'list'}), name="get_user_courses"),
    path('<int:user_id>/get_payment/', views.GetUserCoursePayments.as_view({'get': 'list'}),
         name="get_user_course_payment"),

    path('<int:user_id>/<str:name>/<int:age>/<int:date_of_birth>/<str:qualification>/<str:place>/update_user/',
         views.UpdateUserDetailsViewSet.as_view({'put': 'update'}), name="update_user"),
    path('<int:course_id>/<str:name>/<int:fees>/update_course/',
         views.UpdateCourseDetailsViewSet.as_view({'put': 'update'}, name="update_course")),
    path('<int:user_course_id>/<int:user_id>/<int:course_id>/update_user_course/',
         views.UpdateUserCourseDetailsViewSet.as_view({'put': 'update'}), name="update_user_course"),
    path('<int:user_id>/<int:course_id>/<int:amount_paid>/update_payment/',
         views.UpdateUserCoursePaymentDetailsViewSet.as_view({'put': 'update'}), name="update_payments"),

    path('<int:user_id>/delete_user/',
         views.DeleteUserDetailsViewSet.as_view({'delete': 'destroy'}), name="delete_user"),
    path('<int:course_id>/delete_course/',
         views.DeleteCourseDetailsViewSet.as_view({'delete': 'destroy'}), name="delete_course"),
    path('<int:user_course_id>/delete_user_course/',
         views.DeleteUserCourseDetailsViewSet.as_view({'delete': 'destroy'}), name="delete_user_course"),
    path('<int:user_course_payment_id>/delete_course_payment/',
         views.DeleteCoursePaymentDetailsViewSet.as_view({'delete': 'destroy'}), name="delete_course_payment"),

    path('<int:user_id>/user_courses_count/',
         views.DeleteUserCounterDetailsViewSet.as_view({'delete': 'destroy'}), name="user_courses_count"),
    path('<int:user_id>/user_course_payment_count/',
         views.DeleteUserCoursePaymentDetailsViewSet.as_view({'delete': 'destroy'}), name="user_course_payment_count")



]

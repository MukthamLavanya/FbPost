from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Course, UserCourse, CoursePayment
from .serializers import UserSerializer, CourseSerializer, UserCourseSerializer, CoursePaymentSerializer


class UserDetailsViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import UserSerializer, ValidateUserSerializer

        validate = ValidateUserSerializer(
            data={
                "name": kwargs["name"],
                "age": kwargs["age"],
                "date_of_birth": kwargs["date_of_birth"],
                "qualification": kwargs["qualification"],
                "place": kwargs["place"]
            })

        if kwargs["age"] <= 0:
            return HttpResponse("Invalid Age")

        if kwargs["date_of_birth"] <= 0:
            return HttpResponse("Invalid Date_of_birth")

        if validate.is_valid(raise_exception=True):
            serializer_obj = UserSerializer(
                data={
                    "name": kwargs["name"],
                    "age": kwargs["age"],
                    "date_of_birth": kwargs["date_of_birth"],
                    "qualification": kwargs["qualification"],
                    "place": kwargs["place"]
                }
            )
            if serializer_obj.is_valid(raise_exception=True):
                user = serializer_obj.save()
                response = user.id
                return HttpResponse(response)


class CourseDetailsViewSet(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CourseSerializer, ValidateCourseSerializer

        validate = ValidateCourseSerializer(
            data={
                "name": kwargs["name"],
                "fees": kwargs["fees"]
            }
        )

        if kwargs["fees"] <= 0:
            return HttpResponse("Invalid Fees")

        if validate.is_valid(raise_exception=True):
            serializer_obj = CourseSerializer(
                data={
                    "name": kwargs["name"],
                    "fees": kwargs["fees"]
                }
            )

        if serializer_obj.is_valid(raise_exception=True):
            course = serializer_obj.save()
            response = course.id
            return HttpResponse(response)


class RegisterCourseDetailViewSet(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CourseSerializer, ValidateUserCourseSerializer

        validate = ValidateUserCourseSerializer(
            data={
                "user_id": kwargs["user_id"],
                "course_id": kwargs["course_id"],
                "name": kwargs["name"],
                "fees": kwargs["fees"]
            }
        )

        if kwargs["fees"] <= 0:
            return HttpResponse("Invalid Fee")

        if validate.is_valid(raise_exception=True):
            serializer_obj = CourseSerializer(
                data={
                    "user_id": kwargs["user_id"],
                    "course_id": kwargs["course_id"],
                    "name": kwargs["name"],
                    "fees": kwargs["fees"]
                }
            )

            if serializer_obj.is_valid(raise_exception=True):
                register_course = serializer_obj.save()
                response = register_course.id
                return HttpResponse(response)


class CreatePaymentDetailsViewSet(viewsets.GenericViewSet):
    queryset = CoursePayment.objects.all()
    serializer_class = CoursePaymentSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CoursePaymentSerializer, ValidateCoursePaymentSerializer

        validate = ValidateCoursePaymentSerializer(
            data={
                "amount_paid": kwargs["amount_paid"],
                "user_id": kwargs["user_id"],
                "course_id": kwargs["course_id"]
            }
        )
        try:
            user = User.objects.get(id=kwargs["user_id"])
        except User.DoesNotExist:
            return HttpResponse("Invalid UserId")

        try:
            course = Course.objects.get(id=kwargs["course_id"])
        except Course.DoesNotExist:
            return HttpResponse("Invalid CourseId")

        if kwargs["amount_paid"] <= 0:
            return HttpResponse("Invalid Amount")

        if validate.is_valid(raise_exception=True):
            serializer_obj = CoursePaymentSerializer(
                data={
                    "user": kwargs["user_id"],
                    "course": kwargs["course_id"],
                    "amount_paid": kwargs["amount_paid"]
                }
            )

            if serializer_obj.is_valid(raise_exception=True):
                payment = serializer_obj.save()
                response = payment.id
                return HttpResponse(response)


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import UserSerializer

        serial_obj = UserSerializer(
            data={
                "name": kwargs["name"],
                "age": kwargs["age"],
                "date_of_birth": kwargs["date_of_birth"],
                "qualification": kwargs["qualification"],
                "place": kwargs["place"]
            }
        )
        if serial_obj.is_valid(raise_exception=True):
            user = serial_obj.save()
            return HttpResponse(user.id)


class CourseViewSet(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CourseSerializer

        serializer_obj = CourseSerializer(
            data={
                "name": kwargs["name"],
                "fees": kwargs["fees"]
            }
        )

        if serializer_obj.is_valid(raise_exception=True):
            course = serializer_obj.save()
            response = course.id
            return HttpResponse(response)


class RegisterCourseViewSet(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CourseSerializer

        serial_obj = CourseSerializer(
            data={
                "user_id": kwargs["user_id"],
                "course_id": kwargs["course_id"],
                "name": kwargs["name"],
                "fees": kwargs["fees"]
            }
        )

        if serial_obj.is_valid(raise_exception=True):
            register_course = serial_obj.save()
            response = register_course.id
            return HttpResponse(response)


class CreatePaymentViewSet(viewsets.GenericViewSet):
    queryset = CoursePayment.objects.all()
    serializer_class = CoursePaymentSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CoursePaymentSerializer

        serial_obj = CoursePaymentSerializer(
            data={
                "user": kwargs["user_id"],
                "course": kwargs["course_id"],
                "amount_paid": kwargs["amount_paid"]
            }
        )

        if serial_obj.is_valid(raise_exception=True):
            payment = serial_obj.save()
            return HttpResponse(payment)


class GetUserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import UserSerializer
        from .models import User

        users = User.objects.all() # UserObj --> Db One row
        serial_obj = UserSerializer(users, many=True)
        response = serial_obj.data
        return HttpResponse(response)


class GetCourseViewSet(viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import CourseSerializer
        from .models import Course

        courses = Course.objects.all()
        serial_obj = CourseSerializer(courses, many=True)
        response = serial_obj.data
        return HttpResponse(response)


class GetUserCoursesViewSet(viewsets.GenericViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import UserCourseSerializer
        from .models import UserCourse

        user_courses = UserCourse.objects.all()
        serial_obj = UserCourseSerializer(user_courses, many=True)
        response = serial_obj.data
        return HttpResponse(response)


class GetCoursePaymentViewSet(viewsets.GenericViewSet):
    queryset = CoursePayment.objects.all()
    serializer_class = CoursePaymentSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import CoursePaymentSerializer
        from .models import CoursePayment

        course_payments = CoursePayment.objects.all()
        serial_obj = CoursePaymentSerializer(course_payments, many=True)
        response = serial_obj.data
        return HttpResponse(response)


class GetUserCourseViewSet(viewsets.GenericViewSet):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import UserCourseSerializer
        from .models import Course, UserCourse

        user_course = UserCourse.objects.filter(user_id=kwargs["user_id"])
        ser = UserCourseSerializer(user_course, many=True)
        return HttpResponse(ser.data)


class GetUserCoursePayments(viewsets.GenericViewSet):
    queryset = CoursePayment.objects.all()
    serializer_class = CoursePaymentSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import CoursePaymentSerializer
        from .models import CoursePayment

        courses = CoursePayment.objects.filter(user_id=kwargs["user_id"])
        ser = CoursePaymentSerializer(courses, many=True)
        return HttpResponse(ser.data)
        # TODO:

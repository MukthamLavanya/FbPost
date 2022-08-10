from rest_framework import serializers

from .models import User, Course, UserCourse, CoursePayment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class UserCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCourse
        fields = '__all__'


class CoursePaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoursePayment
        fields = '__all__'


class ValidateUserSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    age = serializers.IntegerField(required=True)
    date_of_birth = serializers.IntegerField(required=True)
    qualification = serializers.CharField(required=True)
    place = serializers.CharField(required=True)

    class Meta:
        fields = "__all__"


class ValidateCourseSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    fees = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"


class ValidateUserCourseSerializer(serializers.Serializer):
    user = serializers.IntegerField(required=True)
    course = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"


class ValidateCoursePaymentSerializer(serializers.Serializer):
    amount_paid = serializers.IntegerField(required=True)
    user = serializers.IntegerField(required=True)
    course = serializers.IntegerField(required=True)

    class Meta:
        fields = "__all__"

from rest_framework import serializers
from .models import User, Education, Company, Achievement


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Education
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = "__all__"


class ValidateUserSerializer(serializers.Serializer):
    Gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    age = serializers.IntegerField()
    date_of_birth = serializers.DateTimeField()
    gender = serializers.ChoiceField(choices=Gender)

    class Meta:
        fields = "__all__"


class ValidateEducationSerializer(serializers.Serializer):
    education = (
        ('10th', '10th'), ('Intermediate', 'Intermediate'), ('Graduation', 'Graduation')
    )
    education_details = serializers.ChoiceField(choices=education)
    score = serializers.IntegerField()
    institute_name = serializers.CharField(max_length=500)

    class Meta:
        fields = "__all__"


class ValidateCompanySerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=500)
    start_year = serializers.DateField()
    end_year = serializers.DateField(default=None)
    package = serializers.IntegerField()

    class Meta:
        fields = "__all__"


class ValidateAchievementSerializer(serializers.Serializer):
    achievement = serializers.CharField(max_length=500)
    year = serializers.DateField()

    class Meta:
        fields = "__all__"






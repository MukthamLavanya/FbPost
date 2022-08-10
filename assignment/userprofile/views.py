from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import User, Education, Company, Achievement
from .serializers import UserSerializer, EducationSerializer, CompanySerializer, AchievementSerializer


class UserDetailsViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import UserSerializer, ValidateUserSerializer

        validate = ValidateUserSerializer(
            data={
                "first_name": kwargs["first_name"],
                "last_name": kwargs["last_name"],
                "age": kwargs["age"],
                "date_of_birth": kwargs["date_of_birth"],
                "gender": kwargs["gender"]
            }
        )
        if kwargs["age"] <= 0:
            return HttpResponse("Invalid Age")

        if validate.is_valid(raise_exception=True):
            serializer_obj = UserSerializer(
                data={
                    "first_name": kwargs["first_name"],
                    "last_name": kwargs["last_name"],
                    "age": kwargs["age"],
                    "date_of_birth": kwargs["date_of_birth"],
                    "gender": kwargs["gender"]
                }
            )
            if serializer_obj.is_valid(raise_exception=True):
                user = serializer_obj.save()
                response = user.id
                return HttpResponse(response)


class EducationDetailsViewSet(viewsets.GenericViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import EducationSerializer, ValidateEducationSerializer

        validate = ValidateEducationSerializer(
            data={
                "user": kwargs["user_id"],
                "education_details": kwargs["education_details"],
                "score": kwargs["score"],
                "institute_name": kwargs["institute_name"]
            }
        )

        if kwargs["score"] <= 0:
            return HttpResponse("Invalid Score")

        if validate.is_valid(raise_exception=True):
            serializer_obj = EducationSerializer(
                data={
                    "user": kwargs["user_id"],
                    "education_details": kwargs["education_details"],
                    "score": kwargs["score"],
                    "institute_name": kwargs["institute_name"]
                }
            )

            if serializer_obj.is_valid(raise_exception=True):
                education = serializer_obj.save()
                response = education.id
                return HttpResponse(response)


class CompanyDetailsViewSet(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        from .serializers import CompanySerializer, ValidateCompanySerializer

        validate = ValidateCompanySerializer(
            data={
                "user": kwargs["user_id"],
                "company_name": kwargs["company_name"],
                "start_year": kwargs["start_year"],
                "end_year": kwargs["end_year"],
                "package": kwargs["package"]
            }
        )
        if validate.is_valid(raise_exception=True):
            serializer_obj = CompanySerializer(
                data={
                    "user": kwargs["user_id"],
                    "company_name": kwargs["company_name"],
                    "start_year": kwargs["start_year"],
                    "end_year": kwargs["end_year"],
                    "package": kwargs["package"]
                }
            )
            if serializer_obj.is_valid(raise_exception=True):
                company = serializer_obj.save()
                response = company.id
                return HttpResponse(response)


class AchievementDetailsViewSet(viewsets.GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def create(self, request, *args, **kwargs):
        from .serializers import AchievementSerializer, ValidateAchievementSerializer

        validate = ValidateAchievementSerializer(
            data={
                "user": kwargs["user_id"],
                "achievement": kwargs["achievement"],
                "year": kwargs["year"]
            }
        )
        if validate.is_valid(raise_exception=True):
            serializer_obj = AchievementSerializer(
                data={
                    "user": kwargs["user_id"],
                    "achievement": kwargs["achievement"],
                    "year": kwargs["year"]
                }
            )
            if serializer_obj.is_valid(raise_exception=True):
                achievement = serializer_obj.save()
                response = achievement.id
                return HttpResponse(response)


class GetUserDetailsViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import UserSerializer
        from .models import User

        users = User.objects.all()
        serializer_obj = UserSerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetEducationDetailsViewSet(viewsets.GenericViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import EducationSerializer
        from .models import Education

        users = Education.objects.all()
        serializer_obj = EducationSerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetCompanyDetailsViewSet(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        from .serializers import CompanySerializer
        from .models import Company

        users = Company.objects.all()
        serializer_obj = CompanySerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetAchievementDetailsViewSet(viewsets.GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import AchievementSerializer
        from .models import Achievement

        users = Achievement.objects.all()
        serializer_obj = AchievementSerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetUserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import UserSerializer
        from .models import User

        user = User.objects.filter(id=kwargs["user_id"])
        serializer_obj = UserSerializer(user, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetUserEducationDetailsViewSet(viewsets.GenericViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import EducationSerializer
        from .models import Education

        users = Education.objects.filter(id=kwargs["user_id"])
        serializer_obj = EducationSerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetUserCompanyDetailsViewSet(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def list(self, request, *args, **kwargs):
        from .serializers import CompanySerializer
        from .models import Company

        users = Company.objects.filter(id= kwargs["user_id"])
        serializer_obj = CompanySerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class GetUserAchievementDetailsViewSet(viewsets.GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def list(self, request, *args, **kwargs):
        from .serializers import AchievementSerializer
        from .models import Achievement

        users = Achievement.objects.filter(id=kwargs["user_id"])
        serializer_obj = AchievementSerializer(users, many=True)
        response = serializer_obj.data
        return HttpResponse(response)


class UpdateUserDetailsViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        from .serializers import UserSerializer, ValidateUserSerializer
        from .models import User

        user_obj = User.objects.get(id=kwargs["user_id"])
        validate = ValidateUserSerializer(
            data={
                "first_name": kwargs["first_name"],
                "last_name": kwargs["last_name"],
                "age": kwargs["age"],
                "date_of_birth": kwargs["date_of_birth"],
                "gender": kwargs["gender"]
            }
        )
        if kwargs["age"] <= 0:
            return HttpResponse("Invalid Age")

        if validate.is_valid(raise_exception=True):
            serializer_obj = UserSerializer(
                data={
                    "first_name": kwargs["first_name"],
                    "last_name": kwargs["last_name"],
                    "age": kwargs["age"],
                    "date_of_birth": kwargs["date_of_birth"],
                    "gender": kwargs["gender"]
                }, instance=user_obj
            )
            if serializer_obj.is_valid(raise_exception=True):
                user = serializer_obj.save()
                response = user.id
                return HttpResponse(response)


class UpdateEducationDetailsViewSet(viewsets.GenericViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def update(self, request, *args, **kwargs):
        from .serializers import EducationSerializer, ValidateEducationSerializer
        from .models import Education

        user_obj = Education.objects.get(id=kwargs["user_id"])
        validate = ValidateEducationSerializer(
            data={
                "user": kwargs["user_id"],
                "education_details": kwargs["education_details"],
                "score": kwargs["score"],
                "institute_name": kwargs["institute_name"]
            }
        )
        if kwargs["score"] <= 0:
            return HttpResponse("Invalid Score")

        if validate.is_valid(raise_exception=True):
            serializer_obj = EducationSerializer(
                data={
                    "user": kwargs["user_id"],
                    "education_details": kwargs["education_details"],
                    "score": kwargs["score"],
                    "institute_name": kwargs["institute_name"]
                }, instance=user_obj
            )
            if serializer_obj.is_valid(raise_exception=True):
                education = serializer_obj.save()
                response = education.id
                return HttpResponse(response)


class UpdateCompanyDetailsViewSet(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def update(self, request, *args, **kwargs):
        from .serializers import CompanySerializer, ValidateCompanySerializer

        user_obj = Company.objects.get(id=kwargs["user_id"])
        validate = ValidateCompanySerializer(
            data={
                "user": kwargs["user_id"],
                "company_name": kwargs["company_name"],
                "start_year": kwargs["start_year"],
                "end_year": kwargs["end_year"],
                "package": kwargs["package"]
            }
        )
        if validate.is_valid(raise_exception=True):
            serializer_obj = CompanySerializer(
                data={
                    "user": kwargs["user_id"],
                    "company_name": kwargs["company_name"],
                    "start_year": kwargs["start_year"],
                    "end_year": kwargs["end_year"],
                    "package": kwargs["package"]
                }, instance=user_obj
            )
            if serializer_obj.is_valid(raise_exception=True):
                company = serializer_obj.save()
                response = company.id
                return HttpResponse(response)


class AchievementDetailsViewSet(viewsets.GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def update(self, request, *args, **kwargs):
        from .serializers import AchievementSerializer, ValidateAchievementSerializer

        user_obj = Achievement.objects.get(id=kwargs["user_id"])
        validate = ValidateAchievementSerializer(
            data={
                "user": kwargs["user_id"],
                "achievement": kwargs["achievement"],
                "year": kwargs["year"]
            }
        )
        if validate.is_valid(raise_exception=True):
            serializer_obj = AchievementSerializer(
                data={
                    "user": kwargs["user_id"],
                    "achievement": kwargs["achievement"],
                    "year": kwargs["year"]
                }, instance=user_obj
            )
            if serializer_obj.is_valid(raise_exception=True):
                achievement = serializer_obj.save()
                response = achievement.id
                return HttpResponse(response)


class DeleteUserDetailsViewSet(viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        from .models import User

        users = User.objects.filter(id=kwargs["user_id"])
        response = users.delete()
        return HttpResponse(response)


class DeleteEducationDetailsViewSet(viewsets.GenericViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def destroy(self, request, *args, **kwargs):
        from .models import Education

        users = Education.objects.filter(id=kwargs["user_id"])
        response = users.delete()
        return HttpResponse(response)


class DeleteCompanyDetailsViewSet(viewsets.GenericViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def destroy(self, request, *args, **kwargs):
        from .models import Company

        users = Company.objects.filter(id=kwargs["user_id"])
        response = users.delete()
        return HttpResponse(response)


class DeleteAchievementDetailsViewSet(viewsets.GenericViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer

    def destroy(self, request, *args, **kwargs):
        from .models import Achievement

        users = Achievement.objects.filter(id=kwargs["user_id"])
        response = users.delete()
        return HttpResponse(response)
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    date_of_birth = models.IntegerField() # Birth Year
    qualification = models.CharField(max_length=500)
    place = models.CharField(max_length=500)


class Course(models.Model):
    name = models.CharField(max_length=500)
    fees = models.IntegerField()


class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class CoursePayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    amount_paid = models.IntegerField()


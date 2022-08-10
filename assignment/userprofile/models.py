from django.db import models


class User(models.Model):
    Gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    date_of_birth = models.DateTimeField()
    gender = models.CharField(max_length=200, choices=Gender)


class Education(models.Model):
    education = (
        ('10th', '10th'), ('Intermediate', 'Intermediate'), ('Graduation', 'Graduation')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    education_details = models.CharField(max_length=600, choices=education)
    score = models.IntegerField()
    institute_name = models.CharField(max_length=500)


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=500)
    start_year = models.DateField()
    end_year = models.DateField(default=None)
    package = models.IntegerField()


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.CharField(max_length=500)
    year = models.DateField()






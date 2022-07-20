import datetime

from django.utils import timezone

from django.db import models

from datetime import date


class Class(models.Model):
    name = models.CharField(max_length=200)
    class_id = models.IntegerField()


class Student(models.Model):
    class_stu_id = models.ForeignKey(Class, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    age = models.IntegerField()

"""
first_class = Class.objects.create(name="first", class_id = 1)
>>> first_class.save()
>>> Student.objects.create(class_stu_id = first_class, name="Lavanya", student_id=1234, age=10)
<Student: Student object (1)>
>>> Student.objects.create(class_stu_id = first_class, name="Lakshmi", student_id=1345, age=12)
<Student: Student object (2)>
>>> Student.objects.create(class_stu_id = first_class, name="Ammu", student_id = 1456, age = 14)
<Student: Student object (3)>
>>> Student.objects.create(class_stu_id = first_class, name="Chinni", student_id = 2456, age = 16) 
<Student: Student object (4)>
>>> Student.objects.create(class_stu_id = first_class, name="Bujji", student_id = 2356, age = 18)  
<Student: Student object (5)>


second_class = Class.objects.create(name="second", class_id = 2)
>>> second_class.save()
>>> Student.objects.create(class_stu_id = second_class, name="Bujji", student_id = 2356, age = 18) 
<Student: Student object (6)>
>>> Student.objects.create(class_stu_id = second_class, name="Nirmala", student_id = 1356, age = 17) 
<Student: Student object (7)>
>>> Student.objects.create(class_stu_id = second_class, name="Lav", student_id = 4356, age = 15)     
<Student: Student object (8)>
>>> Student.objects.create(class_stu_id = second_class, name="chinna", student_id = 3356, age = 13) 
<Student: Student object (9)>
>>> Student.objects.create(class_stu_id = second_class, name="chinnu", student_id = 5356, age = 12) 
<Student: Student object (10)>

third_class = Class.objects.create(name="third", class_id = 3)
>>> third_class.save()
>>> Student.objects.create(class_stu_id = third_class, name="Chinnu", student_id=4455, age=12)
<Student: Student object (11)>
>>> Student.objects.create(class_stu_id = third_class, name="Lavu", student_id=4465, age=13)   
<Student: Student object (12)>
>>> Student.objects.create(class_stu_id = third_class, name="Ammu", student_id=5465, age=14) 
<Student: Student object (13)>
>>> Student.objects.create(class_stu_id = third_class, name="Lucky", student_id=5445, age=16) 
<Student: Student object (14)>
>>> Student.objects.create(class_stu_id = third_class, name="Chinni", student_id=5495, age=18) 
<Student: Student object (15)>

fourth_class = Class.objects.create(name="fourth", class_id=4)
>>> fourth_class.save()
>>> Student.objects.create(class_stu_id = fourth_class, name="Lavanya", student_id=1245, age=14)
<Student: Student object (16)>
>>> Student.objects.create(class_stu_id = fourth_class, name="Lakshmi", student_id=1445, age=15)   
<Student: Student object (17)>
>>> Student.objects.create(class_stu_id = fourth_class, name="Nimmi", student_id=1495, age=18)   
<Student: Student object (18)>
>>> Student.objects.create(class_stu_id = fourth_class, name="Bujji", student_id=1595, age=19) 
<Student: Student object (19)>
>>> Student.objects.create(class_stu_id = fourth_class, name="Chinni", student_id=1495, age=20)     
<Student: Student object (20)>

fifth_class = Class.objects.create(name="fifth", class_id = 5)
>>> fifth_class.save()
>>> Student.objects.create(class_stu_id = fifth_class, name="Lakshmi", student_id = 2234, age=15)
<Student: Student object (21)>
>>> Student.objects.create(class_stu_id = fifth_class, name="Lavanya", student_id = 2534, age=17) 
<Student: Student object (22)>
>>> Student.objects.create(class_stu_id = fifth_class, name="Ammu", student_id = 2934, age=18)    
<Student: Student object (23)>
>>> Student.objects.create(class_stu_id = fifth_class, name="Chinni", student_id = 3634, age=20) 
<Student: Student object (24)>
>>> Student.objects.create(class_stu_id = fifth_class, name="Bujji", student_id = 1634, age=22)  
<Student: Student object (25)>

class_name = []               
>>> for i in Classes:
...     class_name.append(i.name)             
>>> class_name
['first', 'second', 'third', 'fourth', 'fifth']

student_name = Student.objects.all()
>>> stu_names = [] 
>>> for i in student_name:
...     stu_names.append(i.name)
stu_names
['Lavanya', 'Lakshmi', 'Ammu', 'Chinni', 'Bujji', 'Bujji', 'Nirmala', 'Lav', 'chinna', 'chinnu', 'Chinnu', 'Lavu', 'Ammu', 'Lucky', 'Chinni', 'Lavanya', 'Lakshmi', 'Nimmi', 'Bujji', 'C
hinni', 'Lakshmi', 'Lavanya', 'Ammu', 'Chinni', 'Bujji']



 student_obj = Student.objects.get(id = 1)
>>> student_1_id = student_obj.student_id
>>> student_1_id
1234
>>> student_1_name = student_obj.name   
>>> student_1_name
'Lavanya'
>>> student_1_age = student_obj.age
>>> student_1_age
10





"""

class Companies(models.Model):
    name = models.CharField(max_length=200)
    company_started = models.DateTimeField('date published')


class Employee(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    id_number = models.IntegerField()

    class Meta:
        unique_together = ("id_number", )


def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Name(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        abstract = True


class Person(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['name']

class Unmanaged(models.Model):
    class Meta:
        abstract = True
        managed = False

class People(CommonInfo, Unmanaged):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta, Unmanaged.Meta):
        pass


class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    id_number= models.IntegerField()
    name = models.CharField(max_length=200)


class Animal(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

"""

p1 = Pet.objects.create(id_number=1, name="p1") 
>>> p1.save()
>>> a1 = Animal.objects.create(pet = p1, name="a1")
>>> a1.save()
>>> p2 = Pet.objects.create(id_number=2, name="p2") 
>>> p2.save()
>>> p3 = Pet.objects.create(id_number=3, name="p3") 
>>> p3.save()
>>> a2 = Animal.objects.create(pet = p2, name="a2") 
>>> a2.save()
>>> a3 = Animal.objects.create(pet = p3, name="a3") 
>>> a3.save()
>>>                        
Animal.objects.all()                            
<QuerySet [<Animal: Animal object (1)>, <Animal: Animal object (2)>, <Animal: Animal object (3)>]>
>>> Pet.objects.all()
<QuerySet [<Pet: Pet object (3)>, <Pet: Pet object (4)>, <Pet: Pet object (5)>]>

Animal.objects.filter(pet__name__icontains = "p") 
<QuerySet [<Animal: Animal object (1)>, <Animal: Animal object (2)>, <Animal: Animal object (3)>]>
>>> from django.db import connection 
>>> connection.queries
[{'sql': 'INSERT INTO "company_animal" ("pet_id", "name") SELECT NULL, \'a1\' RETURNING "company_animal"."id"', 'time': '0.000'}, {'sql': 'INSERT INTO "company_animal" ("pet_id", "name
") SELECT NULL, \'a1\' RETURNING "company_animal"."id"', 'time': '0.000'}, {'sql': 'INSERT INTO "company_pet" ("id_number", "name") SELECT 1, \'p1\' RETURNING "company_pet"."id"', 'tim
e': '0.000'}, {'sql': 'UPDATE "company_pet" SET "id_number" = 1, "name" = \'p1\' WHERE "company_pet"."id" = 3', 'time': '0.000'}, {'sql': 'INSERT INTO "company_animal" ("pet_id", "name
") SELECT 3, \'a1\' RETURNING "company_animal"."id"', 'time': '0.000'}, {'sql': 'UPDATE "company_animal" SET "pet_id" = 3, "name" = \'a1\' WHERE "company_animal"."id" = 1', 'time': '0.
015'}, {'sql': 'INSERT INTO "company_pet" ("id_number", "name") SELECT 2, \'p2\' RETURNING "company_pet"."id"', 'time': '0.000'}, {'sql': 'UPDATE "company_pet" SET "id_number" = 2, "na
me" = \'p2\' WHERE "company_pet"."id" = 4', 'time': '0.000'}, {'sql': 'INSERT INTO "company_pet" ("id_number", "name") SELECT 3, \'p3\' RETURNING "company_pet"."id"', 'time': '0.000'},
 {'sql': 'UPDATE "company_pet" SET "id_number" = 3, "name" = \'p3\' WHERE "company_pet"."id" = 5', 'time': '0.000'}, {'sql': 'INSERT INTO "company_animal" ("pet_id", "name") SELECT 4, 
\'a2\' RETURNING "company_animal"."id"', 'time': '0.000'}, {'sql': 'UPDATE "company_animal" SET "pet_id" = 4, "name" = \'a2\' WHERE "company_animal"."id" = 2', 'time': '0.016'}, {'sql'
: 'INSERT INTO "company_animal" ("pet_id", "name") SELECT 5, \'a3\' RETURNING "company_animal"."id"', 'time': '0.000'}, {'sql': 'UPDATE "company_animal" SET "pet_id" = 5, "name" = \'a3
\' WHERE "company_animal"."id" = 3', 'time': '0.016'}, {'sql': 'SELECT "company_animal"."id", "company_animal"."pet_id", "company_animal"."name" FROM "company_animal" LIMIT 21', 'time'
: '0.000'}, {'sql': 'SELECT "company_pet"."id", "company_pet"."id_number", "company_pet"."name" FROM "company_pet" LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "company_animal"."id", "
company_animal"."pet_id", "company_animal"."name" FROM "company_animal" INNER JOIN "company_pet" ON ("company_animal"."pet_id" = "company_pet"."id") WHERE "company_pet"."name" LIKE \'%
1%\' ESCAPE \'\\\' LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "company_animal"."id", "company_animal"."pet_id", "company_animal"."name" FROM "company_animal" INNER JOIN "company_pet"
 ON ("company_animal"."pet_id" = "company_pet"."id") WHERE "company_pet"."name" LIKE \'%a2%\' ESCAPE \'\\\' LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "company_animal"."id", "company
_animal"."pet_id", "company_animal"."name" FROM "company_animal" INNER JOIN "company_pet" ON ("company_animal"."pet_id" = "company_pet"."id") WHERE "company_pet"."name" LIKE \'%a%\' ES
CAPE \'\\\' LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "company_animal"."id", "company_animal"."pet_id", "company_animal"."name" FROM "company_animal" LIMIT 21', 'time': '0.000'}, {'
sql': 'SELECT "company_animal"."id", "company_animal"."pet_id", "company_animal"."name" FROM "company_animal" INNER JOIN "company_pet" ON ("company_animal"."pet_id" = "company_pet"."id
") WHERE "company_pet"."name" LIKE \'%p%\' ESCAPE \'\\\' LIMIT 21', 'time': '0.000'}, {'sql': 'SELECT "company_animal"."id", "company_animal"."pet_id", "company_animal"."name" FROM "co
mpany_animal" INNER JOIN "company_pet" ON ("company_animal"."pet_id" = "company_pet"."id") WHERE "company_pet"."name" LIKE \'%1%\' ESCAPE \'\\\' LIMIT 21', 'time': '0.000'}, {'sql': 'S
ELECT "company_animal"."id", "company_animal"."pet_id", "company_animal"."name" FROM "company_animal" INNER JOIN "company_pet" ON ("company_animal"."pet_id" = "company_pet"."id") WHERE
 "company_pet"."name" LIKE \'%p%\' ESCAPE \'\\\' LIMIT 21', 'time': '0.000'}]
>>> initial = len(connection.queries)
>>> initital 
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'initital' is not defined
>>> initial
23
>>> animals = Animal.objects.all() 
>>> animals
<QuerySet [<Animal: Animal object (1)>, <Animal: Animal object (2)>, <Animal: Animal object (3)>]>
>>> for each in animals:
...     print(each.name)
...     print(each.id)
... 
a1
1
a2
2
a3
3
>>> final = len(connection.queries)
>>> final
25
>>> print(final-initial)
2
>>>

>>> from django.db import connection
>>> connection.queries
[]

>>> from company.models import *
>>> p1 = Pet.objects.create(id_number=1, name="p1") 
>>> p1.save()
>>> a1 = Animal.objects.create(pet = p1, name="a1")
>>> a1.save()
>>> p2 = Pet.objects.create(id_number=2, name="p2")  
>>> p2.save()
>>> a2 = Animal.objects.create(pet = p2, name="a2")  
>>> a2.save()
>>> p3 = Pet.objects.create(id_number=3, name="p3")  
>>> p3.save()
>>> a3 = Animal.objects.create(pet = p3, name="a3")  
>>> a3.save()
>>> 
>>> connection.queries
[{'sql': 'INSERT INTO "company_pet" ("id_number", "name") SELECT 1, \'p1\' RETURNING "company_pet"."id"', 'time': '0.016'}, {'sql': 'UPDATE "company_pet" SET "id_number" = 1, "name" = 
\'p1\' WHERE "company_pet"."id" = 6', 'time': '0.000'}, {'sql': 'INSERT INTO "company_animal" ("pet_id", "name") SELECT 6, \'a1\' RETURNING "company_animal"."id"', 'time': '0.015'}, {'
sql': 'UPDATE "company_animal" SET "pet_id" = 6, "name" = \'a1\' WHERE "company_animal"."id" = 4', 'time': '0.016'}, {'sql': 'INSERT INTO "company_pet" ("id_number", "name") SELECT 2, 
\'p2\' RETURNING "company_pet"."id"', 'time': '0.000'}, {'sql': 'UPDATE "company_pet" SET "id_number" = 2, "name" = \'p2\' WHERE "company_pet"."id" = 7', 'time': '0.000'}, {'sql': 'INS
ERT INTO "company_animal" ("pet_id", "name") SELECT 7, \'a2\' RETURNING "company_animal"."id"', 'time': '0.016'}, {'sql': 'UPDATE "company_animal" SET "pet_id" = 7, "name" = \'a2\' WHE
RE "company_animal"."id" = 5', 'time': '0.000'}, {'sql': 'INSERT INTO "company_pet" ("id_number", "name") SELECT 3, \'p3\' RETURNING "company_pet"."id"', 'time': '0.000'}, {'sql': 'UPD
ATE "company_pet" SET "id_number" = 3, "name" = \'p3\' WHERE "company_pet"."id" = 8', 'time': '0.000'}, {'sql': 'INSERT INTO "company_animal" ("pet_id", "name") SELECT 8, \'a3\' RETURN
ING "company_animal"."id"', 'time': '0.000'}, {'sql': 'UPDATE "company_animal" SET "pet_id" = 8, "name" = \'a3\' WHERE "company_animal"."id" = 6', 'time': '0.000'}]
>>> initial = len(connection.queries)
>>> initial
12
>>> Animal.objects.filter(pet__name__icontains="p").select_related("pet")
<QuerySet [<Animal: Animal object (1)>, <Animal: Animal object (2)>, <Animal: Animal object (3)>, <Animal: Animal object (4)>, <Animal: Animal object (5)>, <Animal: Animal object (6)>]
>
>>> animals = Animal.objects.filter(pet__name__icontains="p").select_related("pet") 
>>> for i in animals:
...     print(i.name)
...     print(i.id)
... 
a1
1
a2
2
a3
3
a1
4
a2
5
a3
6
>>>
>>> final = len(connection.queries)
>>> final
14
>>> result = final-initial
>>> result
2
>>>



"""



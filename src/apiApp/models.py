from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # for python 2
    def __unicode__(self):
        return self.user.username

    # for python 3
    def __str__(self):
        return self.user.username


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=15, unique=True)
    dept_id = models.ForeignKey('Department', on_delete=models.CASCADE)

    # for python 2
    def __unicode__(self):
        return self.user.username

    # for python 3
    def __str__(self):
        return self.user.username


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    # for python 2
    def __unicode__(self):
        return self.name

    # for python 3
    def __str__(self):
        return self.name


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    dept_id = models.ForeignKey('Department', on_delete=models.CASCADE)
    teacher_id = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=50, blank=True)    # optional
    academic_yr = models.IntegerField(null=False)   # 2015 -> 2015-16, 2016 -> 2016-2017
    year = models.IntegerField(null=False)  # 1->First Year, 2->Second Year
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    students = models.ManyToManyField(Student)

    class Meta:
        unique_together = ('name', 'academic_yr', 'year', 'teacher_id')

    # for python 2
    def __unicode__(self):
        return self.name

    # for python 3
    def __str__(self):
        return self.name


class Lecture(models.Model):
    lect_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    lect_no = models.IntegerField(blank=True)
    duration = models.IntegerField(null=False)
    comment = models.CharField(max_length=50, blank=True)    # optional
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    students = models.ManyToManyField(Student)

    # for python 2
    def __unicode__(self):
        return self.lect_id

    # for python 3
    def __str__(self):
        return self.lect_id


# for class student images
def upload_location(instance, filename):
    return "%s/%s" % (instance.student_id, filename)


class StudentImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_location)
    type = models.IntegerField()

    class Meta:
        unique_together = ('student_id', 'type')

    # for python 2
    def __unicode__(self):
        return str(self.image_id)

    # for python 3
    def __str__(self):
        return str(self.image_id)




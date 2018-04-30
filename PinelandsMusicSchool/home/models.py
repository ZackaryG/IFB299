from django.db import models

# Initialise options for choice fields
CONTACT_PREF_OPTIONS = (
    ('p', 'Phone'),
    ('e', 'Email'),
    ('f', 'Facebook'),
)

STUDENT_TYPE_OPTIONS = (
    ('n', 'New'),
    ('o', 'Old'),
)


# Create your models here.
class School(models.Model):
    streetNumber = models.IntegerField()
    streetName = models.CharField(max_length=100)
    postcode = models.IntegerField()
    suburb = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    facebook = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contactPref = models.CharField(choices=CONTACT_PREF_OPTIONS, max_length=1)
    studentType = models.CharField(choices=STUDENT_TYPE_OPTIONS, max_length=1)
    schoolID = models.ForeignKey(School, default='1', on_delete=models.CASCADE)


class Parent(models.Model):
    studentID = models.ForeignKey(Student, default='1', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField()
    facebook = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)


class Preference(models.Model):
    studentID = models.ForeignKey(Student, default='1', on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)


class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    facebook = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contactPref = models.CharField(choices=CONTACT_PREF_OPTIONS, max_length=1)
    payScale = models.IntegerField()
    bank = models.CharField(max_length=100)
    bsb = models.IntegerField()
    accountNumber = models.IntegerField()
    schoolID = models.ForeignKey(School, default='1', on_delete=models.CASCADE)


class Language(models.Model):
    teacherID = models.ForeignKey(Teacher, default='1', on_delete=models.CASCADE)
    language = models.CharField(max_length=100)


class Skill(models.Model):
    teacherID = models.ForeignKey(Teacher, default='1', on_delete=models.CASCADE)
    skill = models.CharField(max_length=100)


class Qualification(models.Model):
    teacherID = models.ForeignKey(Teacher, default='1', on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)


class Contract(models.Model):
    studentID = models.ForeignKey(Student, default='1', on_delete=models.CASCADE)
    teacherID = models.ForeignKey(Teacher, default='1', on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    lessonType = models.CharField(max_length=100)
    lessonDuration = models.IntegerField()
    lessonCost = models.IntegerField()
    totalNumberOfLessons = models.IntegerField()
    totalLessonCost = models.IntegerField()


class Lesson(models.Model):
    studentID = models.ForeignKey(Student, default='1', on_delete=models.CASCADE)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()


class Manager(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    facebook = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contactPref = models.CharField(choices=CONTACT_PREF_OPTIONS, max_length=1)
    payScale = models.IntegerField()
    bank = models.CharField(max_length=100)
    bsb = models.IntegerField()
    accountNumber = models.IntegerField()
    schoolID = models.ForeignKey(School, default='1', on_delete=models.CASCADE)


class Admin(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    facebook = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contactPref = models.CharField(choices=CONTACT_PREF_OPTIONS, max_length=1)
    payScale = models.IntegerField()
    bank = models.CharField(max_length=100)
    bsb = models.IntegerField()
    accountNumber = models.IntegerField()


class Owner(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    DOB = models.DateField()
    gender = models.CharField(max_length=100)
    phone = models.IntegerField()
    facebook = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contactPref = models.CharField(choices=CONTACT_PREF_OPTIONS, max_length=1)
    payScale = models.IntegerField()
    bank = models.CharField(max_length=100)
    bsb = models.IntegerField()
    accountNumber = models.IntegerField()


class Instrument(models.Model):
    type = models.CharField(max_length=100)
    size = models.IntegerField()
    quality = models.CharField(max_length=100)
    available = models.BooleanField()
    rentalPrice = models.IntegerField()
    salePrice = models.IntegerField()


class InstrumentHire(models.Model):
    studentID = models.ForeignKey(Student, default='1', on_delete=models.CASCADE)
    instrumentID = models.ForeignKey(Instrument, default='1', on_delete=models.CASCADE)
    lessonID = models.ForeignKey(Lesson, default='1', on_delete=models.CASCADE)

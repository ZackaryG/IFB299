from django.test import TestCase
from login.models import *
from login.forms import *
from django.contrib.auth import authenticate

# Run tests in shell by entering the following command:
# 'python manage.py test login

# Create your tests here.
class UserModelTests(TestCase):
    global email, first_name, last_name, dob, password

    email = 'ass@butt.com'
    first_name = 'Heywood'
    last_name = 'Jablowme'
    dob = '1969-08-02'
    password = 'qqqgqq'

    def test_create_teacher(self):
        '''
        Tests creation of a teacher
        :return:
        '''
        teacher = Member.objects.create_teacher(email=email, first_name=first_name, last_name = last_name, dob=dob, password=password)

        self.assertIsInstance(teacher, Member) # Test teacher was successfully created
        assert(teacher.is_teacher == True) # Test member is teacher
        assert(teacher.get_full_name() == first_name + ' ' + last_name) # Test name was created successfully
        assert(teacher.get_first_name() == first_name)
        assert(teacher.get_last_name() == last_name)
        assert(teacher.get_dob() == dob) # Test DOB was recorded successfully
        assert(teacher.get_email() == email) # Test email was recorded

    def test_create_student(self):
        '''
        Tests creation of a student
        :return:
        '''
        student = Member.objects.create_student(email, first_name, last_name, dob, password)

        self.assertIsInstance(student, Member)
        assert(student.is_teacher == False)
        assert (student.get_full_name() == first_name + ' ' + last_name)  # Test name was created successfully
        assert (student.get_first_name() == first_name)
        assert (student.get_last_name() == last_name)
        assert (student.get_dob() == dob)  # Test DOB was recorded successfully
        assert (student.get_email() == email)  # Test email was recorded

    def test_login(self):
        '''
        Tests authentication of a member
        '''
        user = Member.objects.create_student(email, first_name, last_name, dob, password)

        # Failed login
        wrongUser = authenticate(username = email, password = 'wrongpassword')
        assert(user != wrongUser)

        #
        rightUser = authenticate(username = email, password = password)
        assert(rightUser == user)

class TestTimetables(TestCase):
    def createStudent(self):
        student = Member.objects.create_student('fafafa@afafaf.com', 'Toby', 'Larone', '1997-12-10',
                                                'godsavethequeensheisa****')
        return student

    def createTeacher(self):
        teacher = Member.objects.create_teacher('juicy@ass.com', 'Suqma', 'Diq', '1969-04-17', 'qqqgqq')
        return teacher


    def testTimetableCreation(self):
        '''
        Test successful creation of timetable
        '''
        student = self.createStudent()

        timetable = Timetable.objects.create(member = student)
        self.assertIsInstance(timetable, Timetable)
        assert(timetable.member == student)

    def testTimetableSet(self):
        '''
        Test successful setting of timetable
        '''
        student = self.createStudent()
        timetable = Timetable.objects.create(member = student)

        timetableList = [Timetable.MON, Timetable.WED, Timetable.FRI] # List of desired timetable times

        timetable.setTimetable(timetableList) # Set timetable

        # Assert day availability is what we expect
        assert(timetable.mon == True)
        assert(timetable.tue == False)
        assert(timetable.wed == True)
        assert(timetable.thu == False)
        assert(timetable.fri == True)
        assert(timetable.sat == False)
        assert(timetable.sun == False)

# class TestForms(TestCase):
#     global valid_data
#
#     valid_data = {'email': 'ass@butt.com',
#                   'first_name': 'Heywood',
#                   'last_name': 'Jablowme',
#                   'dob': '1969-08-02',
#                   'password1': 'qqqgqq',
#                   'password2': 'qqqgqq'}
#
#
#     def test_admin_form(self):
#         form = UserAdminCreationForm(valid_data)
#         assert(form.is_valid())
#
#     def test_registration_form(self):
#         form = RegisterForm(valid_data)
#
#         print(form.is_valid())
#         print(form.clean_email())
#         print(form.clean_first_name())
#         print(form.clean_last_name())
#         print(form.clean_dob())
#         print(form.clean_password2())

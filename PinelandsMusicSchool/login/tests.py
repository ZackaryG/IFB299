from django.test import TestCase
from login.models import UserManager, Member
from login.forms import UserAdminCreationForm
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
        teacher = Member.objects.create_teacher(email=email, first_name=first_name, last_name = last_name, dob=dob, password=password)

        self.assertIsInstance(teacher, Member) # Test teacher was successfully created
        assert(teacher.is_teacher == True) # Test member is teacher
        assert(teacher.get_full_name() == first_name + ' ' + last_name) # Test name was created successfully
        assert(teacher.get_first_name() == first_name)
        assert(teacher.get_last_name() == last_name)
        assert(teacher.get_dob() == dob) # Test DOB was recorded successfully
        assert(teacher.get_email() == email) # Test email was recorded

    def test_create_student(self):
        student = Member.objects.create_student(email, first_name, last_name, dob, password)

        self.assertIsInstance(student, Member)
        assert(student.is_teacher == False)
        assert (student.get_full_name() == first_name + ' ' + last_name)  # Test name was created successfully
        assert (student.get_first_name() == first_name)
        assert (student.get_last_name() == last_name)
        assert (student.get_dob() == dob)  # Test DOB was recorded successfully
        assert (student.get_email() == email)  # Test email was recorded

    def test_login(self):
        user = Member.objects.create_student(email, first_name, last_name, dob, password)

        # Failed login
        wrongUser = authenticate(username = email, password = 'wrongpassword')
        assert (user != wrongUser)

        #
        rightUser = authenticate(username = email, password = password)
        assert(rightUser == user)

class TestForms(TestCase):

    def test_admin_form(self):
        form = UserAdminCreationForm()

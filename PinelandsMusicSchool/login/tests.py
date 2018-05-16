from django.test import TestCase
from login.models import UserManager, Member

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
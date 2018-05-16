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

    def test_create_user(self):
        user = Member.objects.create_user(email=email, first_name=first_name, last_name = last_name, dob=dob, password=password)

        self.assertIsInstance(user, Member)
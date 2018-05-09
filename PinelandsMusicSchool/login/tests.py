from django.test import TestCase
from login.models import *

# Run tests in shell by entering the following command:
# 'python manage.py test login

# Create your tests here.
class UserModelTests(TestCase):
    global email, first_name, last_name, password

    email = 'ass@butt.com'
    first_name = 'Heywood'
    last_name = 'Jablowme'

    def test_create_user(self):
        manager = UserManager()
        user = manager.create_user(email='ass@butt.com', first_name='Heywood', password = 'qqqgqq')

        assert(type(user) == "<class 'Member'>")
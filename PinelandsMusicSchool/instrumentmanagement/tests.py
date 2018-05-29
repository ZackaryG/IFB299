from django.test import TestCase
from instrumentmanagement.models import Instrument
from login.models import Member

# Create your tests here.
def createInstrument():
    return Instrument.objects.create(type='Guitar', size='Small', quality=Instrument.NEW, rental_price=5.50, sale_price=100.00)

def createStudent():
    email = 'ass@butt.com'
    first_name = 'Heywood'
    last_name = 'Jablowme'
    dob = '1969-08-02'
    password = 'qqqgqq'

    return Member.objects.create_student(email, first_name, last_name, dob, password)

class InstrumentTests(TestCase):
    def test_create_instrument(self):
        '''
        Test if instrument is successfully created, and is avaliable
        '''
        guitar = createInstrument()
        self.assertIsInstance(guitar, Instrument)
        assert(guitar.is_avaliable() == True)

    def test_assign_to_existing_student(self):
        '''
        Tests assigning & unassigning instrument to student
        '''
        student = createStudent() # Create student
        guitar = createInstrument() # Create instrument

        guitar.set_assigned_student(student.get_username())

        assert(guitar.assigned_student == student.get_username())
        assert(guitar.is_avaliable() == False)

        # Reset owner to none
        guitar.reset_owner()
        assert(guitar.assigned_student == Instrument.NO_OWNER) # Instrument now has no owner
        assert(guitar.is_avaliable() == True) # Instrument now avaliable

    def test_assign_to_nonexisting_student(self):
        '''
        Tests assigning instrument to student, when input username does not exist
        :return:
        '''
        guitar = createInstrument()

        self.assertRaises(ValueError, lambda: guitar.set_assigned_student('holy@moses.com')) # ValueError Raised

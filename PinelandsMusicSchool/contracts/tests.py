from django.test import TestCase
from login.models import Member
from contracts.models import Contract
from django.utils import timezone

# Create your tests here.

class ContractTests(TestCase):

    def testContractCreation(self):
        student = Member.objects.create_student('ass@butt.com', 'Heywood', 'Jablowme', '1997-12-10', 'qqqgqq')
        teacher = Member.objects.create_teacher('butt@ass.com', 'Anhass', 'Rhamarr', '1969-04-17', 'qqqgqq')

        contract = Contract(teacher=teacher, student=student)
        self.assertIsInstance(contract, Contract)




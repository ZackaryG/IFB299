from django.test import TestCase
from login.models import Member
from contracts.models import Contract, AcceptenceError
from django.utils import timezone

# Create your tests here.

class ContractTests(TestCase):

    def createStudentTeacher(self):
        student = Member.objects.create_student('ass@butt.com', 'Heywood', 'Jablowme', '1997-12-10', 'qqqgqq')
        teacher = Member.objects.create_teacher('butt@ass.com', 'Anhass', 'Rhamarr', '1969-04-17', 'qqqgqq')
        return student, teacher

    def testContractCreation(self):
        student, teacher = self.createStudentTeacher()
        '''
        Test creation of contract between student and teacher
        '''
        contract = Contract(teacher=teacher, student=student)
        contract.save()
        self.assertIsInstance(contract, Contract)

    def testContractVerification(self):
        student, teacher = self.createStudentTeacher()
        contract = Contract(teacher=teacher, student=student)
        contract.save()

        # Case: Neither accepted
        # Expected: Acceptance Error Raised
        with self.assertRaises(AcceptenceError) as context:
            contract.start_contract()
            self.assertTrue('This is broken' in str(context.AcceptanceError))

        assert (contract.status == contract.PENDING)

        # Case: Student not accepted
        # Expected: Acceptance Error Raised
        contract.teacher_accepted = True
        contract.student_accepted = False
        contract.save()

        with self.assertRaises(AcceptenceError) as context:
            contract.start_contract()
            self.assertTrue('This is broken' in str(context.AcceptanceError))

        assert (contract.status == contract.PENDING)

        # Case: Teacher not accepted
        # Expected: Acceptance Error Raised
        contract.teacher_accepted = False
        contract.student_accepted = True
        contract.save()

        with self.assertRaises(AcceptenceError) as context:
            contract.start_contract()
            self.assertTrue('This is broken' in str(context.AcceptanceError))

        assert (contract.status == contract.PENDING)

        # Case: Both accepted
        contract.teacher_accepted = True
        contract.student_accepted = True

        contract.start_contract()
        contract.save()

        assert(contract.student_accepted==True)
        assert(contract.teacher_accepted==True)
        assert(contract.status == contract.ACTIVE)

    def testSearch(self):
        student, teacher = self.createStudentTeacher()

        contract = Contract(teacher=teacher, student=student)
        contract.save()

        foundContract = Contract.objects.filter(student=student, teacher = teacher)
        assert(contract == foundContract[0])
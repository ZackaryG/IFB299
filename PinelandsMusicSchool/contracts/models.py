from django.db import models
from login.models import Member
from django.utils import timezone

class AcceptenceError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class Contract(models.Model):
    teacher = models.ForeignKey(Member, related_name='Teacher', on_delete=models.DO_NOTHING, default=None, null=False)
    student = models.ForeignKey(Member, related_name='Student', on_delete=models.DO_NOTHING, default=None, null=False)

    # Possible statuses of contract
    PENDING = 'P'
    ACTIVE = 'A'
    COMPLETED = 'C'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (ACTIVE, 'Active'),
        (COMPLETED, 'Completed'),
    )

    # Fields indicating contract acceptance
    teacher_accepted = models.BooleanField(default=False)
    student_accepted = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=PENDING)

    start_date = models.DateField('Contract Start Date', auto_now_add=True)

    def __str__(self):
        id = str(self.id)
        teacher_name = self.teacher.get_last_name()
        student_name = self.student.get_last_name()

        return("Contract " + id + ' between ' + teacher_name + ' and ' + student_name)

    def start_contract(self):
        '''
        Starts contract, if both student and teacher have accepted contract.
        :return: Throws AcceptanceError if neither have accepted
        '''
        if not self.student_accepted:
            raise AcceptenceError('Student has not accepted contract')
        elif not self.teacher_accepted:
            raise AcceptenceError('Teacher has not accepted contract')
        else:
            self.status = self.ACTIVE
            self.start_date = timezone.now()

    def end_contract(self):
        '''
        Ends contract, if contract is currently active
        Flags contract as inactive, and participants as not accepted.
        Flags contract as completed.
        '''
        if self.statue == self.ACTIVE:
            self.teacher_accepted = False
            self.student_accepted = False
            self.status = self.COMPLETED



from django.db import models
from login.models import Member
from django.utils import timezone


class Contract(models.Model):
    teacher = models.ForeignKey(Member, related_name='Teacher', on_delete=models.DO_NOTHING, default=None, null=False)
    student = models.ForeignKey(Member, related_name='Student', on_delete=models.DO_NOTHING, default=None, null=False)

    # Fields indicating contract acceptance
    teacher_accepted = models.BooleanField(default=False)
    student_accepted = models.BooleanField(default=False)
    contract_active = models.BooleanField(default=False)

    start_date = models.DateField('Contract Start Date', auto_now_add=True)

    def start_contract(self):
        if not self.student_accepted:
            raise(PermissionError, 'Student has not accepted contract')
        elif not self.teacher_accepted:
            raise(PermissionError, 'Teacher has not accepted contract')
        else:
            self.contract_active = True
            self.start_date = timezone.now()



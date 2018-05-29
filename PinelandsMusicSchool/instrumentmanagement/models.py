from django.db import models
from login.models import Member

# Create your models here.
class Instrument(models.Model):
    '''
    Django model representing an instrument in inventory
    '''

    # Instrument quality choices
    NEW = 'n'
    USED = 'u'
    UNSPECIFIED = 'p'
    QUALITY_CHOICES = ((NEW, 'New'),
                       (USED, 'Used'),
                       (UNSPECIFIED, 'Unspecified')
                       )

    type = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quality = models.CharField(max_length=2,
                               choices = QUALITY_CHOICES,
                               default = UNSPECIFIED)
    is_sold = models.BooleanField(default = False)
    rental_price = models.FloatField(default = 12)
    sale_price = models.FloatField(default = 100)
    assigned_student = models.CharField(max_length=100, default='None')

    def is_avaliable(self):
        '''
        Checks if instrument is avaliable (has no assigned student/is not sold)
        :return: True if instrument has no assigned student, and is not sold.
        '''
        return self.assigned_student == 'None' and not self.is_sold

    def set_assigned_student(self, student_username):
        try:
            assert(Member.objects.filter(email=student_username).exists() == True)
        except:
            raise ValueError('Student does not exist')

        self.assigned_student = student_username



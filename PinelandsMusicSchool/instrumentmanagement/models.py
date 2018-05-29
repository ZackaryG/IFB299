from django.db import models
from login.models import Member

# Create your models here.
class Instrument(models.Model):
    '''
    Django model representing an instrument in inventory
    '''

    # CONSTANTS
    # Instrument quality choices
    NEW = 'n'
    USED = 'u'
    UNSPECIFIED = 'p'
    QUALITY_CHOICES = ((NEW, 'New'),
                       (USED, 'Used'),
                       (UNSPECIFIED, 'Unspecified')
                       )

    NO_OWNER = 'None'

    # FIELDS
    type = models.CharField(max_length=100) # Instrument type (guitar, ukelele, banjo, etc)
    size = models.CharField(max_length=100) # Size of instrument
    quality = models.CharField(max_length=2,
                               choices = QUALITY_CHOICES,
                               default = UNSPECIFIED) # Quality of instrument (New, or used)
    is_sold = models.BooleanField(default = False)
    rental_price = models.FloatField(default = 12)
    sale_price = models.FloatField(default = 100)
    assigned_student = models.CharField(max_length=100, default=NO_OWNER)

    def is_avaliable(self):
        '''
        Checks if instrument is avaliable (has no assigned student/is not sold)
        :return: True if instrument has no assigned student, and is not sold.
        '''
        return self.assigned_student == self.NO_OWNER and not self.is_sold

    def set_assigned_student(self, student_username):
        '''
        Assigns instrument to a student.
        Throws a ValueError if no student exists
        :param student_username: username (email) of student
        '''
        try:
            assert(Member.objects.filter(email=student_username).exists() == True)
        except:
            raise ValueError('Student does not exist')

        self.assigned_student = student_username

    def reset_owner(self):
        '''
        Resets assigned student to None
        '''
        self.assigned_student = self.NO_OWNER



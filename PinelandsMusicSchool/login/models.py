from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.first_name = first_name
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, first_name, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )

        user.first_name = first_name
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            first_name,
            password=password,
        )

        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

    # def create_student(self, email, first_name, password):
    #     user = self.create_user(
    #         email,
    #         first_name,
    #         password=password,
    #     )
    #
    #     user.user_permissions.set()

class Member(AbstractBaseUser):
    email = models.EmailField(
        verbose_name = 'email address',
        max_length = 255,
        unique = True,
    )

    # Personal details
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()

    objects = UserManager()

    # Permissions
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'dob'] # Email & Password are required by default.

    # User metadata
    # class Meta:
    #     permissions = (
    #         ('student', 'Student'),
    #         ('teacher', 'Teacher'),
    #     )

    def get_full_name(self):
        '''
        Getter method for user's name
        :return: user's name
        '''
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def __str__(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

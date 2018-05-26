from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import datetime
from .models import Member


class RegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField(label='Confirm password')

    class Meta:
        model = Member
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        '''
        Checks if email is unique
        :return: email, if email is valid.
                 Raises an error if email is taken.
        '''
        email = self.cleaned_data.get('email')
        qs = Member.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(label ='First Name')
    last_name = forms.CharField(label='Last Name')
    password1 = forms.CharField(label='Password')
    password2 = forms.CharField(label='Password confirmation')

    class Meta:
        model = Member
        fields = ('email', 'first_name', 'last_name', 'dob')

    def clean_first_name(self):
        '''
        Check first name is valid (only characters or spaces).
        Raises Validation error if name is not valid.
        :return: First name, if first name is valid
        '''
        first_name = self.cleaned_data.get('first_name')
        if not all(x.isalpha() or x.isspace() for x in first_name):
            raise forms.ValidationError('First name is invalid. Please only use letters, and spaces.')
        return first_name

    def clean_last_name(self):
        '''
        Check first name is valid (only characters or spaces).
        Raises Validation error if name is not valid.
        :return: First name, if first name is valid
        '''
        last_name = self.cleaned_data.get('last_name')
        if not all(x.isalpha() or x.isspace() for x in last_name):
            raise forms.ValidationError('Last name is invalid. Please only use letters, and spaces.')
        return last_name

    def clean_dob(self):
        '''
        Check if Date of Birth entered is a valid format ('yyyy-mm-dd')
        Raises Validation Error
        :return: DOB, if valid.
        '''
        dob = self.cleaned_data.get('dob')
        day, month, year = dob.split('-')

        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            raise forms.ValidationError('Date is invalid. Please use the format "yyyy-mm-dd"')

        return dob

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Member
        fields = ('email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
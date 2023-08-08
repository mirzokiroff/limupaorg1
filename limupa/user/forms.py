from django.forms import Form, CharField, EmailField
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from user.models import User, OurTeam
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(ModelForm):
    confirm_password = CharField(max_length=255)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'address', 'postcode', 'password', 'confirm_password', 'username')

    def clean_password(self):
        if self.cleaned_data['password'] != self.data['confirm_password']:
            raise ValidationError('Password didn\'t match ')
        return make_password(self.cleaned_data['password'])


class ContactForm(Form):
    name = CharField(max_length=255)
    email = EmailField(max_length=255)
    subject = CharField(max_length=255)
    text = CharField()


class CustomLoginForm(AuthenticationForm):
    pass


class OurTeamForm(ModelForm):
    class Meta:
        model = OurTeam
        fields = ['name', 'job', 'image', 'instagram', 'email', 'twitter', 'linkedin', 'facebook']

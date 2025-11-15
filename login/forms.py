from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Partner, OrgType, AvaType


# create a user
class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# user auth
class LoginForm (AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

class PartnerForm (forms.ModelForm):
    class Meta:
        model = Partner
        fields = [
            'partner_Name',
            'organization_Type',
            'available_Resources',
            'email',
            'phone_Number',
        ]

class BotForm (forms.Form):
    prompt = forms.CharField(max_length=4000)

class OrgForm (forms.ModelForm):
    class Meta:
        model = OrgType
        fields = ['organization_type']

class AvaForm (forms.ModelForm):
    class Meta:
        model = AvaType
        fields = ['available_resources']
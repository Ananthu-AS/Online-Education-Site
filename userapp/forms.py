from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from userapp.models import registration
from django import forms

# existing user details
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']
 
# additional user details       
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=registration
        fields=['photo','phone']
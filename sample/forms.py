from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from sample.models import *

class EnquiryForm(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields = "__all__"
class signupform(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2')


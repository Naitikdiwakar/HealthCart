from django import forms
from customer.models import *


class MyUserForm(forms.ModelForm):
    class Meta:
        model=MyUser
        fields=('password','first_name','last_name','email','country','state','mobile_number')
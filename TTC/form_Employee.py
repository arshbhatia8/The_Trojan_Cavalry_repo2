from django import forms
from TTC.models import Employee

class NewUser(forms.ModelForm):
    class Meta():
        model=Employee
        fields='__all__'

    
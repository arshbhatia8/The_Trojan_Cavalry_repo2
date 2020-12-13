from django import forms
from TTC.models import Employer

class NewEmployer(forms.ModelForm):
    class Meta():
        model=Employer
        fields='__all__'

    
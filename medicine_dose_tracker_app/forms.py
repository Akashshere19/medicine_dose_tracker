from .models import *
from django import forms


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = "__all__"
        exclude = ['user']
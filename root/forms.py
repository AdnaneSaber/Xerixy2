from django import forms
from .models import Leads


class ContactForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = "__all__"

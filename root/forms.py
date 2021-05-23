from django import forms
from .models import Lead
from django.utils.translation import ugettext_lazy as _
from captcha.fields import ReCaptchaField


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Lead
        fields = "__all__"
        labels = {
            'firstName': _('First name'),
            'lastName': _('Last name'),
            'mail': _('Mail address'),
            'phone': _('Phone number'),
            'interestedBy': _('Intereseted by'),
            'message': _('Your message'),
        }
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'First name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'mail': forms.TextInput(attrs={'placeholder': 'Mail address'}),
            'message': forms.Textarea(attrs={'placeholder': 'Type your message...'}),
        }

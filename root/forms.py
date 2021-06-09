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
            'interestedBy': _('Interested by'),
            'message': _('Your message'),
        }
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': _('First name')}),
            'phone': forms.TextInput(attrs={'placeholder': _('Phone number')}),
            'lastName': forms.TextInput(attrs={'placeholder': _('Last name')}),
            'mail': forms.TextInput(attrs={'placeholder': _('Mail address')}),
            'message': forms.Textarea(attrs={'placeholder': _('Type your message here')}),
        }

import re
from django import template
from ..models import UserInfo 

register = template.Library()

def rep(value):
    user = UserInfo.objects.first()
    variables = {
        "site_name":user.nom_sur_site,
        "email":user.email,
        "phone":user.phone,
        "adress":user.adresse_local
    }
    output = str(value)
    for i in variables:
        output = output.replace(f'{{{{{i}}}}}',variables[i])
    return output


from django.utils.translation import ugettext
@register.filter(name='template_trans')
def template_trans(text):
    try:
        return ugettext(text)
    except Exception as e:
        return text

register.filter('vars', rep)
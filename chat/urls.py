# urls.py

from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView,
    )

app_name ='chat'

urlpatterns = [
    # replace <string_endpoint> with the one you created above
    re_path(r'^01e7925bc8e21a3c5b8406e52da5e414465631dd638f24c946e1fe8157f1/$', FacebookWebhookView.as_view(), name='webhook'),
]



# After replacing your pattern would look something like this:
# re_path(r'^d33300c2f7df8016b9f49f53179f9cae51/$', FacebookWebhookView.as_view(), name='webhook'),
# urls.py

from django.urls import re_path
from django.contrib import admin

from .views import (
    FacebookWebhookView,
    )

app_name ='chat'

urlpatterns = [
    # replace <string_endpoint> with the one you created above
    re_path(r'^d8db68392956fcc31d9a91579fa144707d4f8d6f2119d993fcd985509e95/$', FacebookWebhookView.as_view(), name='webhook'),
]



# After replacing your pattern would look something like this:
# re_path(r'^d33300c2f7df8016b9f49f53179f9cae51/$', FacebookWebhookView.as_view(), name='webhook'),
from django.urls import path
from . import views


urlpatterns = [
    path('adnane/', views.adnane, name='adnane'),
]

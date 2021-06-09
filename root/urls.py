from django.urls import path
from . import views


urlpatterns = [
    path('phone/', views.phoneClick_view.as_view(), name='phoneApi'),
]

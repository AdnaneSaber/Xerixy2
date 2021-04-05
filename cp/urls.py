"""cp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from root import views as root_view

urlpatterns = [
    path('', root_view.index),
    path('api/', include('root.urls')),
    path('admin/', admin.site.urls),
    path('contact/', root_view.contact_view),
    path('services/', root_view.services),
    path('gallery/', root_view.gallery_view),
    path('news/', root_view.news),
    path('about/<str:link>', root_view.seoLinks_view),
    path('services/<str:service_url>/', root_view.service_view, name="service"),
]

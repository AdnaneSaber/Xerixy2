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
from django.urls import path, include
from root import views as root_view
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', root_view.index, name="index"),
    path('api/', include('root.urls')),
    path('chat/', include('chat.urls')),
    path('adminX/', admin.site.urls),
    path('adminXerixyUpdate/', root_view.update_view, name='update'),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),
    path('contact/', root_view.contact_view, name='contact'),
    path('services/', root_view.services, name='services'),
    path('maintenance/', include('maintenance_mode.urls')),
    path('gallery/', root_view.gallery_view),
    path('news/', root_view.news),
    path('about/<str:link>', root_view.seoLinks_view),
    path('services/<str:service_url>/', root_view.service_view, name="service"),
    path('todos/', include('tasks.urls')),
    path('<str:page_url>/', root_view.page_view, name="page")
]

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
from root.sitemaps import NewSitemap, PageSitemap, SeoLinkSitemap, ServiceSitemap, StaticSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns

sitemaps = {
    'page':PageSitemap,
    'blog':NewSitemap,
    'seo':SeoLinkSitemap,
    'services':ServiceSitemap,
    'static':StaticSitemap
}

urlpatterns = [
    path('adminX/', admin.site.urls),
]
urlpatterns +=i18n_patterns(
    
    path('', root_view.index, name="index"),
    path('api/', include('root.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('chat/', include('chat.urls')),
    path('adminXerixyUpdate/', root_view.update_view, name='update'),
    path('robots.txt', TemplateView.as_view(
        template_name="robots.txt", content_type="text/plain")),
    path('contact/', root_view.contact_view, name='contact'),
    path('services/', root_view.services, name='services'),
    path('maintenance/', include('maintenance_mode.urls')),
    path('gallery/', root_view.gallery_view, name='gallery'),
    path('news/', root_view.news, name='news'),
    path('new/<str:post_url>', root_view.new, name='new'),
    path('frequent/<str:link>', root_view.seoLinks_view, name="seo"),
    path('services/<str:service_url>/', root_view.service_view, name="service"),
    path('todos/', include('tasks.urls')),
    path('<str:page_url>/', root_view.page_view, name="page"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    prefix_default_language=False,
)

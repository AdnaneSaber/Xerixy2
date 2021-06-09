from django.contrib.sitemaps import Sitemap
from .models import Page, SeoLink, Service,  New
from django.urls import reverse


class PageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Page.objects.all()

    def location(self, obj):
        return '/%s' % (obj.page_url)


class NewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return New.objects.all()

    def location(self, obj):
        return '/news/%s' % (obj.post_url)


class SeoLinkSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return SeoLink.objects.all()

    def location(self, obj):
        return '/frequent/%s' % (obj.url)


class ServiceSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Service.objects.all()

    def location(self, obj):
        return '/services/%s' % (obj.service_url)


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['index', 'contact', 'gallery']

    def location(self, item):
        return reverse(item)

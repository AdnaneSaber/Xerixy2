import os
from datetime import datetime
from django.utils.html import escape, mark_safe
from django.conf import settings
from django.db import models
from unidecode import unidecode
from django.core.validators import RegexValidator
from PIL import Image


def assetSaver(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (datetime.now(), ext)
    return os.path.join(settings.BASE_DIR / "static", filename)


def faviconGenerator(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'logo.{ext}'
    icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (64, 64),
                  (57, 57), (72, 72), (114, 114), (120, 120), (144, 144), (152, 152)]
    imag = Image.open(instance.logo)
    imgext = str(instance.logo).split('.')[-1]
    for size in icon_sizes:
        s = list(size)
        imag = imag.resize((s[0], s[1]), Image.ANTIALIAS)
        imgName = urlFormater(instance.logo)
        imag.save(os.path.join(settings.BASE_DIR /
                               "static/logo", f'favicon-{s[0]}.png'))
        imag.save(os.path.join(settings.BASE_DIR /
                               "static/logo", f'favicon.ico'))
    found = os.path.join(settings.BASE_DIR / "static/logo", filename)
    if os.path.exists(found):
        os.remove(found)
    return os.path.join(settings.BASE_DIR / "static/logo", filename)


class UserInfo(models.Model):
    email = models.EmailField(unique=True, blank=False)
    phone = models.CharField(max_length=64, blank=False,
                             validators=[
                                 RegexValidator(
                                     regex='^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$',
                                     message="Merci d'entrer un numéro de téléphone valide, comme : (0123456789 or +1234567890)",
                                 ),
                             ])
    nom_sur_site = models.CharField(max_length=10, blank=False)
    adresse_local = models.TextField()
    logo = models.ImageField(
        upload_to=faviconGenerator, blank=True)

    def __str__(self):
        return self.email

# I need to make this pages integrate in a
# class pages(models.Model):
#     page_title = models.CharField(max_length=255, blank=False)
#     page_content = models.TextField(blank=True)


class Maintenance(models.Model):
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        f = open(os.path.join(settings.BASE_DIR / "cp",
                              "maintenance_mode_state.txt"), mode="w")
        f.write(str(int(self.status)))
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Status: {self.status}"


class New(models.Model):
    post_title = models.CharField(max_length=255, blank=False)
    post_url = models.CharField(
        max_length=255, null=False, blank=True, unique=True)
    post_content = models.TextField(blank=False)
    post_image = models.ImageField(
        upload_to=assetSaver, default='/no_image.jpg')
    post_time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.post_url:
            self.post_url = urlFormater(self.post_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_title


class Combination(models.Model):
    keywords = models.TextField()
    prepositions = models.TextField()
    locations = models.TextField()

    def __str__(self):
        return "Keywords and locations"

    def save(self, *args, **kwargs):
        keywords = str(self.keywords).replace("\r", "").split('\n')
        prepositions = str(self.prepositions).replace("\r", "").split('\n')
        locations = str(self.locations).replace("\r", "").split('\n')
        p_c = []
        for i in range(len(locations)):
            p_c.append(f"{prepositions[i]} {locations[i]}")
        SeoLink.objects.all().delete()
        for y in keywords:
            for j in p_c:
                SeoLink.objects.create(title=f"{y} {j}")
        super().save(*args, **kwargs)


class Service(models.Model):
    service_title = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    service_url = models.CharField(
        max_length=255, null=False, blank=True, unique=True)
    service_meta_title = models.CharField(blank=True,
                                          max_length=60)
    service_meta_description = models.CharField(blank=True,
                                                max_length=160)
    service_content = models.TextField(blank=False, default="pas de contenu..")
    service_image = models.ImageField(
        upload_to=assetSaver, default='/no_service.jpg')
    service_image_alt = models.CharField(max_length=30, blank=True)

    @property
    def Image_preview(self):
        if self.service_image:
            return mark_safe('<img src="/static{}" width="75" height="50" />'.format(self.service_image.url))
        return ""

    def __str__(self):
        return self.service_title

    def save(self, *args, **kwargs):
        if not self.service_url:
            self.service_url = urlFormater(self.service_title)
        super().save(*args, **kwargs)


def urlFormater(sentence):
    accented_string = u'{}'.format(sentence)
    unaccented_string = unidecode(accented_string)
    removedSpace = unaccented_string.replace(" ", "-")
    lowerCase = str(removedSpace).lower()
    return lowerCase


class Gallery(models.Model):
    image_title = models.CharField(max_length=255, blank=False, null=False)
    image_alt = models.CharField(blank=True, max_length=255)
    image_description = models.CharField(blank=True, max_length=255)
    image = models.ImageField(
        upload_to=assetSaver, default='/no_image.jpeg')

    @property
    def Image_preview(self):
        if self.image:
            return mark_safe('<img src="/static{}" width="75" height="50" />'.format(self.image.url))
        return ""


class SeoLink(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    url = models.CharField(max_length=255, null=False, blank=True, unique=True)
    content = models.TextField(blank=False, default="pas de contenu..")
    meta_title = models.CharField(blank=True,
                                  max_length=60)
    meta_description = models.CharField(blank=True,
                                        max_length=160)

    def save(self, *args, **kwargs):
        if not self.url:
            self.url = urlFormater(self.title)
        super().save(*args, **kwargs)

    @property
    def contentLength(self):
        if self.content:
            return mark_safe(str(len(self.content.split()))+" Mots")
        return str(0)+" Mots"

    def __str__(self):
        return self.title


class Lead(models.Model):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64, blank=False)
    phone = models.CharField(max_length=64, blank=False,
                             validators=[
                                 RegexValidator(
                                     regex='^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$',
                                     message='Please enter a valid phone number like : (0123456789 or +1234567890)',
                                 ),
                             ])
    mail = models.EmailField(blank=False)
    interestedBy = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.TextField(blank=False)
    send_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mail


class GitAccount(models.Model):
    userName = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    repository = models.CharField(max_length=25)
    upatePassword = models.CharField(max_length=50)

    def __str__(self):
        return self.userName


class PhoneClick(models.Model):
    page = models.CharField(max_length=255)
    # should be edited
    location = models.CharField(max_length=255)
    # should be edited
    geo_location = models.CharField(max_length=255)
    click_date = models.DateTimeField(auto_now_add=True)


class Page(models.Model):
    page_title = models.CharField(max_length=255)
    page_meta_title = models.CharField(blank=True,
                                       max_length=60)
    page_meta_description = models.TextField(blank=True,
                                             max_length=160)
    page_url = models.CharField(
        max_length=255, null=False, blank=True, unique=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['my_order']

    def save(self, *args, **kwargs):
        if not self.page_url:
            self.page_url = urlFormater(self.page_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.page_title


class PageContent(models.Model):
    content_title = models.CharField(max_length=255)
    content = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    def __str__(self):
        return self.content_title

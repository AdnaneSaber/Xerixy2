from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Page, PageContent, Service, Gallery, SeoLink, UserInfo, New, PhoneClick, GitAccount
from django.conf import settings
from .forms import ContactForm
from .serializers import PhoneSerializer
from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
import git
from django.contrib.gis.geoip2 import GeoIP2
import requests
import json
import os
import subprocess
import shlex


def form_view(request):
    context = {}
    context.update(bases())
    form = ContactForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        location = request.POST.get("location")
        firstname = form.cleaned_data.get("firstName")
        lastname = form.cleaned_data.get("lastName")
        message = form.cleaned_data.get("message")
        mail = form.cleaned_data.get("mail")
        interestedBy = form.cleaned_data.get("interestedBy")
        phone = form.cleaned_data.get("phone")
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        subject = f"NEW LEAD at {now}"
        siteName = context['user'].nom_sur_site
        messageContent = \
            f"""
                Hello Dear client,
                this is a mail from {siteName}, you just received a lead, I'll let you check it out.

                from : {firstname} {lastname}
                interested by : {interestedBy}
                phone number : {phone}
                email : {mail}
                message : {message}
                location : {location}
                --------------------------------------------------------
                Well that was all for today,
                you received this mail at {now}
                _{siteName}_
                Have a good day
        """
        emain_to = UserInfo.objects.first().email
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, messageContent, email_from,
                  [emain_to, ])
        context['success'] = True
        form.save()
        form = ContactForm()
    context['form'] = form
    return context

def contact_view(request):
    context = {"self": "contact"}.copy()
    context.update(bases())
    context.update(form_view(request))
    return render(request, "contact.html", context)


def bases():
    gallery = Gallery.objects.all()
    services = Service.objects.all()
    link_query = SeoLink.objects.all()
    news = New.objects.all()
    page = Page.objects.all()
    seo = SeoLink.objects.all()
    user = UserInfo.objects.first()
    return {"gallery": gallery, "services": services, "seoLinks": link_query, 'news': news, 'seo': seo, 'user': user, 'pages': page}


def index(request):
    context = {"self": "index"}.copy()
    context.update(bases())
    context.update(form_view(request))
    return render(request, "index.html", context=context)


def service_view(request, service_url):
    queryset = Service.objects.get(service_url=service_url)
    context = {"service": queryset}.copy()
    context.update(bases())
    context.update(form_view(request))
    if not queryset:
        raise Http404
    return render(request, "service.html", context=context)


def services(request):
    context = {"self": "services"}.copy()
    context.update(bases())
    context.update(form_view(request))
    return render(request, "services.html", context=context)


def news(request):
    context = {"self": "news"}.copy()
    context.update(bases())
    context.update(form_view(request))
    return render(request, "news.html", context=context)


def new(request, post_url):
    context = {"self": "new"}.copy()
    query = New.objects.get(post_url=post_url)
    context = {"new":query}
    context.update(bases())
    context.update(form_view(request))
    return render(request, "new.html", context=context)


def gallery_view(request):
    context = {"self": "gallery"}.copy()
    context.update(bases())
    context.update(form_view(request))
    return render(request, "gallery.html", context=context)


def seoLinks_view(request, link):
    link_query = SeoLink.objects.get(url=link)
    context = {"link": link_query}.copy()
    context.update(bases())
    context.update(form_view(request))
    if not link_query:
        raise Http404
    return render(request, "seo.html", context=context)


class phoneClick_view(APIView):
    def get(self, request):
        clicks = PhoneClick.objects.all()
        serializer = PhoneSerializer(clicks, many=True)
        return Response(serializer.data)


def update_view(request):
    if request.method == 'GET':
        return render(request, "git_update.html")
    elif request.method == 'POST':
        git = GitAccount.objects.first()
        if request.POST.get('password') == git.upatePassword:
            msg = subprocess.run(shlex.split(
                f'git pull https://{git.userName}:{git.password}@github.com/{git.userName}/{git.repository}'), cwd="/home/adn/chauffepro/", stdout=subprocess.PIPE)
            context = msg.stdout.decode('utf-8')
        else:
            context = "<span style='color: #f00'>Error</span>"
        return render(request, "git_update.html", context={'output': context})
    else:
        raise Http404


def page_view(request, page_url):
    try:
        queryset = Page.objects.get(page_url=page_url)
    except Page.DoesNotExist:
        queryset = None
    if not queryset:
        raise Http404
    contents = PageContent.objects.filter(page=queryset.id)
    data = []
    for i in range(contents.count()):
        data.append({
            "id": contents[i].id,
            "content_title": contents[i].content_title,
            "content": contents[i].content,
        })
    context = {"self": queryset, "data": data}.copy()
    context.update(bases())
    context.update(form_view(request))
    template = "page.html"
    for file in os.listdir(os.path.join(settings.BASE_DIR / __package__ / "templates")):
        if file == f"page-{queryset.id}.html":
            template = file
    return render(request, template, context=context)

from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Service, Gallery, seoLink, UserInfo, New, phoneClick
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


def contact_view(request):
    context = {"self": "contact"}.copy()
    context.update(bases())
    form = ContactForm(request.POST or None, request.FILES or None)
    location_json = json.loads(requests.get("https://ipinfo.io").text)
    location = f"{location_json['city']} - {location_json['country']}"
    if form.is_valid():
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
    return render(request, "contact.html", context)


def bases():
    gallery = Gallery.objects.all()
    services = Service.objects.all()
    link_query = seoLink.objects.all()
    news = New.objects.all()
    user = UserInfo.objects.first()
    return {"gallery": gallery, "services": services, "seoLinks": link_query, 'news': news, 'user': user}


def index(request):
    context = {"self": "index"}.copy()
    context.update(bases())
    return render(request, "index.html", context=context)


def service_view(request, service_url):
    queryset = Service.objects.get(service_url=service_url)
    context = {"service": queryset}.copy()
    context.update(bases())
    if not queryset:
        raise Http404
    return render(request, "service.html", context=context)


def services(request):
    context = {"self": "services"}.copy()
    context.update(bases())
    return render(request, "services.html", context=context)


def news(request):
    context = {"self": "news"}.copy()
    context.update(bases())
    return render(request, "news.html", context=context)


def news(request):
    context = {"self": "news"}.copy()
    context.update(bases())
    return render(request, "news.html", context=context)


def gallery_view(request):
    context = {"self": "gallery"}.copy()
    context.update(bases())
    return render(request, "gallery.html", context=context)


def seoLinks_view(request, link):
    link_query = seoLink.objects.get(url=link)
    context = {"link": link_query}.copy()
    context.update(bases())
    if not link_query:
        raise Http404
    return render(request, "seo.html", context=context)


class phoneClick_view(APIView):
    def get(self, request):
        clicks = phoneClick.objects.all()
        serializer = PhoneSerializer(clicks, many=True)
        return Response(serializer.data)


def update_view(request):
    if request.method == 'GET':
        return render(request, "git_update.html")
    elif request.method == 'POST':
        # if request.POST.get('password') == 'Adnane05022020Salm@':
        if request.POST.get('password') == 'adn':
            # g = git.cmd.Git('/home/adn/chauffepro/')
            # git.config_writer().set_value("user", "name", "AdnaneSaber").release()
            # git.config_writer().set_value("user", "email", "adnanesaber15@gmail.com").release()
            # msg = g.pull()
            # os.system('sudo git pull;sudo systemctl restart apache2;')
            # msg = os.popen('sudo git pull;sudo systemctl restart apache2;').read()
            # context = msg
            result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
            
            # proc = subprocess.Popen(
            #     shlex.split('sudo git --git-dir=/home/adn/chauffepro/.git pull'), stdout=subprocess.PIPE, shell=True)
            # (out, err) = proc.communicate()
            # # print(out)
            context = result.stdout
        else:
            context = "<span style='color: #ccc'>Error</span>"
        return render(request, "git_update.html", context={'output': context})
    else:
        raise Http404

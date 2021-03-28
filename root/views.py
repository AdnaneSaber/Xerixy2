from django.core.mail import BadHeaderError, send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Service, Gallery, seoLinks, UserInfos
from django.conf import settings
from .forms import ContactForm
from datetime import datetime


def contact_view(request):
    context = {"self": "contact"}.copy()
    context.update(bases())
    form = ContactForm(request.POST or None, request.FILES or None)
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
        messageContent = \
            f"""
        Hello Dear client,
        this is a mail from SAMS, you just received a lead, I'll let you check it out.

        from : {firstname} {lastname}
        interested by : {interestedBy}
        phone number : {phone}
        email : {mail}
        message : {message}
        --------------------------------------------------------
        Well that was all for today,
        you received this mail at {now}
        _SAMS_
        Have a good day
        """
        emain_to = UserInfos.objects.first().email
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
    link_query = seoLinks.objects.all()
    return {"gallery": gallery, "services": services, "seoLinks": link_query}


def index(request):
    context = {"self": "index"}.copy()
    context.update(bases())
    return render(request, "base.html", context=context)


def service_view(request, service_url):
    queryset = Service.objects.filter(service_url=service_url)
    context = {"service": queryset}.copy()
    context.update(bases())
    if not queryset:
        raise Http404
    return render(request, "service.html", context=context)


def services(request):
    context = {"self": "services"}.copy()
    context.update(bases())
    return render(request, "services.html", context=context)


def gallery_view(request):
    context = {"self": "gallery"}.copy()
    context.update(bases())
    return render(request, "gallery.html", context=context)


def seoLinks_view(request, link):
    link_query = seoLinks.objects.filter(url=link)
    context = {"link": link_query}.copy()
    context.update(bases())
    if not link_query:
        raise Http404
    return render(request, "seo.html", context=context)

# Create your views here.
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from settings import CONTACT_EMAIL

from ez_contact.forms import ContactForm



def contact-send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject =form.cleaned_data['subject']
            message =  form.cleaned_data['name'] + '- ' + form.cleaned_data['email'] + '\n' + form.cleaned_data['message']
            from_email = form.cleaned_data['email']
            to = CONTACT_EMAIL
            
            email = EmailMessage(subject, message, from_email, [to])
            email.send()
            
            return HttpResponseRedirect('/contact-success/')
    else:
        form = ContactForm()
        
    return render_to_response('django_ez_contact/contact.html', {'form': form })
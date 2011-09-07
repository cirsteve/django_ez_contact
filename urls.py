from django.conf.urls.defaults import *

from django_ez_contact.views import contact

class ContactSuccessView(TemplateView):
    template_name = 'django_ez_contact/contact-success.html'

urlpatterns = patterns('',
    url(r'contact-form/$', contact, name='contact-form-send'),
    url(r'contact-success/(?P<pk>[-\d]+)/$', ContactSuccessView.as_view(), name='contact-form-success'),
    
)
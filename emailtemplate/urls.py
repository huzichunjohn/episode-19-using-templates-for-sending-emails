from django.conf.urls import patterns, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^email_one/$', 'main.views.email_one', name='emailone'),
    url(r'^email_two/$', 'main.views.email_two', name='emailtwo'),

    url(r'^$', TemplateView.as_view(template_name='main/index.html'), name='home'),
)

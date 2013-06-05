from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

def email_one(request):
    subject = "I am a text email"
    to = ['buddy@buddylindsey.com']
    from_email = 'test@example.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    message = render_to_string('main/email/email.txt', ctx)

    EmailMessage(subject, message, to=to, from_email=from_email).send()

    return HttpResponse('email_one')

def email_two(request):
    subject = "I am an HTML email"
    to = ['buddy@buddylindsey.com']
    from_email = 'test@example.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    message = get_template('main/email/email.html').render(Context(ctx))
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('email_two')


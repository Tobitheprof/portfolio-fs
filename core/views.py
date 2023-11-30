from django.shortcuts import render
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from portfolio import settings


def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        context = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message,
        }
        message = get_template('mail.html').render(context)

        msg = EmailMessage(
            'Email Received',
            message,
            'Oluwatobi Ekundayo',
            [email],
        )
        msg.content_subtype="html"
        msg.send()

        message2 = get_template('mail2.html').render(context)
        msg2 = EmailMessage(
            "Message from your portfolio",
            message2,
            'Oluwatobi Ekundayo',
            [settings.DEFAULT_FROM_EMAIL]
        )
        msg2.content_subtype="html"
        msg2.send()




    return render(request, 'index.html')

# Create your views here.

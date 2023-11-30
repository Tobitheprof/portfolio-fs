from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import EmailMessage
from portfolio import settings
from django.contrib import messages

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            context = {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }

            # Send emails within the same request
            send_email(context)

            messages.success(request, "Hey, I've received your message and I'll respond as soon as I can. While you wait, here are some cool cat videos for you to watch")

    return render(request, 'index.html')

def send_email(context):
    message = get_template('mail.html').render(context)
    msg = EmailMessage(
        'Email Received',
        message,
        'Oluwatobi Ekundayo',
        [context['email']],
    )
    msg.content_subtype = "html"
    msg.send()

    message2 = get_template('mail2.html').render(context)
    msg2 = EmailMessage(
        "Message from your portfolio",
        message2,
        'Oluwatobi Ekundayo',
        [settings.DEFAULT_FROM_EMAIL]
    )
    msg2.content_subtype = "html"
    msg2.send()

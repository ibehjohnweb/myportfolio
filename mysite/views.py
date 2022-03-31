from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        name = request.POST['fullname']
        email = request.POST['email']
        message = request.POST['message']
        contacting = "Name: " + name + " \nMessage: " + message + " \nEmail:" + email
        # send an email
        send_mail(
            'Contact on portfolio',  # subject
            contacting,  # message
            email,  # from email
            ['ibehjohn16@gmail.com'],  # to email
            fail_silently=False,
        )
        return render(request, 'home.html', {'name': name})
    else:
        return render(request, 'home.html', {})


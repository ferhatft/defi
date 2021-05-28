from django.shortcuts import render,redirect

from .models import Contact
from django.core.mail import send_mail
from .forms import ContactForm
# Create your views here.


def contacview(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name        = form.cleaned_data['name']
            email       = form.cleaned_data['email']
            message     = form.cleaned_data['message']
            subject     = form.cleaned_data['subject']
            # send_mail (
            #     subject, # subject
            #     'Gönderen = ' + name + email + '\n' + message , #message
            #     '', #from email
            #     ['',], # To email    
            # )

            # send_mail (
            #    'Defi ', # subject
            #     'İletişime geçtiğiniz için teşekkür ederiz en kısa sürede size dönüş yapılacaktır', #message
            #     '', #from email
            #     [email], # To email    
            # )

            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, "contac.html", context)

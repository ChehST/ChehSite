from django.shortcuts import render

from .forms import Offers_MailForm


def info(request):
    return render(request, 'Offer/info.html')

def contacts(request):
    return render(request, 'Offer/contacts.html')

def sent_OfferMail(request):
    form = Offers_MailForm

    data = {
        'form':form
    }

    return render(request, 'Offer/mailto.html', data)


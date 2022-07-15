from django.shortcuts import render

from .forms import Offers_MailForm


def info(request):
    return render(request, 'Offer/info.html')

def contacts(request):
    error = ''
    if request.method == 'POST':
        form = Offers_MailForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Ошибка в форме'

    form = Offers_MailForm

    data ={
      'form':form,
      'error':error,
    }
    return render(request, 'Offer/contacts.html',data)

from django.shortcuts import render

def info(request):
    return render(request, 'Offer/info.html')

def contacts(request):
    return render(request, 'Offer/contacts.html')


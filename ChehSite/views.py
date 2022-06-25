from django.shortcuts import render

def pageNotFound(request,exception):
    return render(request,'Offer/404.html', status=404)

def page_e500(request):
    return render(request,'Offer/500.html',status=500)

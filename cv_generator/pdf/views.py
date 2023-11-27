from django.shortcuts import render


# Create your views here.


def accept_views(request):
    return render(request, "pdf/accept.html")

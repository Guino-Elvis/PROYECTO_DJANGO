from django.shortcuts import render


def home(request):
    return render(request, "crm/pages/home.html")


def producto(request):
    return render(request, "crm/pages/producto.html")

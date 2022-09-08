from tkinter import W
from django.shortcuts import render
from .models import Cliente

# Create your views here.


def home(request):

    if request.user.is_authenticated:
        client = Cliente.objects.get(user=request.user.id)
        return render(request, "clientes/index.html", {'current_user': client})

    return render(request, "clientes/index.html")

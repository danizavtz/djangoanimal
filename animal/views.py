from django.shortcuts import render

from django.http import HttpResponse

from .models import Animal

def index(request):
    animal = Animal.objects.order_by('?').first()

    context={
        "animal": animal,
        "especie": animal.especie
    }
    return render(request, 'animal/index.html', context)

from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request,'index.html')

def mostrar_servicio(request):
    datos = {
        "servicio": "lavado de vehiculos: ",
        "costolavado": 10000,

        "cambiaraceite": "Cambiado de aceite: ",
        "costoaceite": 2000,

        "inflarllantas": "Inflar llanta: ",
        "costoinflar": 0
    }
    return render(request, 'about.html', datos)
from django.shortcuts import render
from comunicacion.forms import RadioEnlaceForm
import math

# Constante velocidad de la luz (m/s)
c = 3e8

def calcular_fsl(f, d):
    # FSL = 20*log10(4*pi*d*f/c)
    return 20 * math.log10(4 * math.pi * d * f / c)


def calcular1(request):
    resultado = None
    if request.method == 'POST':
        form = RadioEnlaceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # Extraer datos\ n            data = form.cleaned_data
            Pt = data['potencia_tx']
            pct = data['perdidas_cable_tx']
            Gt = data['ganancia_ant_tx']
            f  = data['frecuencia']
            d  = data['distancia']
            Gr = data['ganancia_ant_rx']
            pcr = data['perdidas_cable_rx']
            Ms = data['margen_sens_rx']
            fad = data['perdidas_adicionales']

            # Cálculos
            fsl = calcular_fsl(f, d)
            margen = Pt - pct + Gt - fsl + Gr - pcr
            pr = Pt - pct + Gt - fsl + Gr - fad
            reserva = margen - Ms

            resultado = {
                'fsl': round(fsl, 2),
                'margen': round(margen, 2),
                'pr': round(pr, 2),
                'reserva': round(reserva, 2),
            }
    else:
        form = RadioEnlaceForm()

    return render(request, 'calcular.html', {
        'form': form,
        'resultado': resultado
    })

def lab(request):
    return render(request, 'Labview.html')
def home(request):
    return render(request,'home.html')
def prueba(request):
    return render(request,'prueba.html')

def mensaje(request):
    return render(request, 'mensaje.html')

def fm(request):
    return render(request,'fm.html')

def calcular(request):
    print("solicitud post no  hecha")
    resultado=0
   
    if request.method== "POST":
        print("solicitud post hecha")
        tiempo_trasnmision= int(request.POST.get("tiempo"))
        tamano_mensaje= int(request.POST.get("tamano"))
        velocidad_transmision= int(request.POST.get("velocidad"))
        opcion=request.POST.get("seleccion")
        if opcion=="1":
            print("resultado= ")
            tiempo_trasnmision=tamano_mensaje/velocidad_transmision
            resultado=tiempo_trasnmision
        elif opcion==2:
            tamano_mensaje=velocidad_transmision*tiempo_trasnmision
            resultado=tamano_mensaje
        elif opcion==3:
            velocidad_transmision=tamano_mensaje/tiempo_trasnmision
            resultado=velocidad_transmision
    if request.method == "GET":
        print("solicitud get hecha")
    print(resultado)
    resultado_no_cero = resultado != 0
    return render(request,'calculadora.html',{"resultado":resultado, 'resultado_no_cero': resultado_no_cero})


def am(request):
    return render(request,'am.html')
def fsk(request):
    return render(request,'fsk.html')
def ask(request):
    return render(request,'ask.html')


def decibeles(request):
    return render(request,'decibeles.html')
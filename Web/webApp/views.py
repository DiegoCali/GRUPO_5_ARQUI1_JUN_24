from django.shortcuts import render

# Create your views here.
iluminacionGeneral = False
iluminacionExterior = False

def test(request):
    return render(request, 'test.html', {'iluminacionGeneral': iluminacionGeneral, 'iluminacionExterior': iluminacionExterior})

def encenderIluminacionGeneral(request):
    global iluminacionGeneral
    if request.method == 'POST':
        iluminacionGeneral = True
    return render(request, 'test.html', {'iluminacionGeneral': iluminacionGeneral, 'iluminacionExterior': iluminacionExterior})
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import DatosGeneralesForm
from datos_socioeconomicos.forms import DatosSocioeconomicosForm
from .models import DatosGenerales
from datos_socioeconomicos.models import DatosSocioeconomicos

@login_required
def index(request, id=None):
    datos_generales = DatosGenerales.objects.filter(user=request.user).first()
    datos_socioeconomicos = None

    if datos_generales:
        datos_socioeconomicos = DatosSocioeconomicos.objects.filter(datos_generales=datos_generales).first()

    if request.method == "POST":
        form = DatosGeneralesForm(request.POST, instance=datos_generales)
        economico = DatosSocioeconomicosForm(request.POST, instance=datos_socioeconomicos)

        if form.is_valid() and economico.is_valid():
            datos_generales = form.save(commit=False)
            datos_generales.user = request.user
            datos_generales.save()
            datos_socioeconomicos, created = DatosSocioeconomicos.objects.update_or_create(
                datos_generales=datos_generales,
                defaults={
                    'ingresos': economico.cleaned_data['ingresos'],
                    'situacion_laboral': economico.cleaned_data['situacion_laboral']
                }
            )

            return redirect('generales')

    else:
        form = DatosGeneralesForm(instance=datos_generales)
        economico = DatosSocioeconomicosForm(instance=datos_socioeconomicos)

    datos_guardados = datos_generales is not None

    return render(request, 'datosgenerales.html', {
        'form': form,
        'economico': economico,
        'datos_guardados': datos_guardados
    })
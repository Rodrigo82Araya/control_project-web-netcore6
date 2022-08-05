from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from app_orden.forms import OrdenesForm
from .models import Orden

#ORDENES====================================================================================
def orden_listar(request):
    ordenes = Orden.objects.all().filter(activo=True)
    pages = request.GET.get('page',1)

    try:
        paginator = Paginator(ordenes, 5)
        ordenes = paginator.page(pages)
    except:
        raise Http404

    data={
        'entity':ordenes,
        'paginator':paginator
    }
    return render(request, 'orden/orden_listar.html',data)

def orden_agregar(request):
    data = {
        'form': OrdenesForm()
    }

    if request.method == 'POST':
        formulario = OrdenesForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'orden/orden_agregar.html',data)

def orden_modificar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    data = {
        'form':OrdenesForm(instance=ordenes)
    }

    if request.method == 'POST':
        formulario = OrdenesForm(data=request.POST, instance=ordenes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            #data["mensaje"] = "Modificado correctamente"
            return redirect(to="orden_listar")
        else:
            data["form"] = formulario          

    return render(request, 'orden/orden_modificar.html', data)

def orden_eliminar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    ordenes.delete()
    return render(request, 'orden/orden_listar.html')

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from app_orden.forms import OrdenesForm
from .models import Orden
from django.contrib import messages

#ORDENES====================================================================================
titulo="Orden"
tituloPlu="Ordenes"

def orden_listar(request):
    ordenes_all = Orden.objects.all().filter(activo=True).order_by('id').reverse()
    filas = 7
    pages = request.GET.get('page',1)    
        
    try:
        paginator = Paginator(ordenes_all, filas)
        ordenes = paginator.page(pages)
        filaInicio= (filas * ordenes.number) - (filas - 1)

        filasTotales = (filas * ordenes.number)  
        if ( filasTotales < ordenes_all.count()): 
            filaFin=filasTotales
        else:
            filaFin=ordenes_all.count()

    except:
        raise Http404

    data={
        'entity':ordenes,
        'paginator':paginator,
        'totalFilas':ordenes_all.count(),
        'filaInicio': filaInicio,
        'filaFin':filaFin,
        'pageTitulo': titulo,
        'pageTituloPlu': tituloPlu,
        'pageAccion': 'Listado',
    }
    return render(request, 'orden/orden_listar.html',data)

def orden_agregar(request):
    data = {
        'form': OrdenesForm(),
        'pageTitulo': titulo,
        'pageTituloPlu': tituloPlu,
        'pageAccion': 'Agregar',
    }

    if request.method == 'POST':
        formulario = OrdenesForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Orden ingresada correctamente")

            redirect("orden_agregar")
        else:
            data["form"] = formulario
            messages.error(request, 'Problemas para ingresar la orden')

    return render(request, 'orden/orden_agregar_modificar.html',data)

def orden_modificar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    data = {
        'form':OrdenesForm(instance=ordenes),
        'pageTitulo': titulo,
        'pageTituloPlu': tituloPlu,
        'pageAccion': 'Modificar',
    }

    if request.method == 'POST':
        formulario = OrdenesForm(data=request.POST, instance=ordenes, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Orden modificada correctamente")

            return redirect("orden_modificar",id)
        else:
            messages.error(request, 'Problemas para modificar la orden')
            data["form"] = formulario

    return render(request, 'orden/orden_agregar_modificar.html', data)

def orden_eliminar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    ordenes.delete()
    return redirect(to='orden_listar')

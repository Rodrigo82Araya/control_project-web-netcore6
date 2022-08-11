from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from app_orden.forms import OrdenesForm, SeguimientoForm
from django.contrib.auth.decorators import login_required
from .models import Orden, Seguimiento
from django.contrib import messages

#ORDENES====================================================================================
titulo="Orden"
tituloPlu="Ordenes"

@login_required(login_url='login')
def orden_listar(request):
    listado_all = Orden.objects.all().filter(activo=True).order_by('-id')
    filas = 7
    pages = request.GET.get('page',1)    
        
    try:
        paginator = Paginator(listado_all, filas)
        listadoPaginador = paginator.page(pages)
        filaInicio= (filas * listadoPaginador.number) - (filas - 1)

        filasTotales = (filas * listadoPaginador.number)  
        if ( filasTotales < listado_all.count()): 
            filaFin=filasTotales
        else:
            filaFin=listado_all.count()

    except:
        raise Http404

    data={
        'entity':listadoPaginador,
        'paginator':paginator,
        'totalFilas':listado_all.count(),
        'filaInicio': filaInicio,
        'filaFin':filaFin,
        'pageTitulo': titulo,
        'pageTituloPlu': tituloPlu,
        'pageAccion': 'Listado',
    }
    return render(request, 'orden/orden_listar.html',data)

@login_required(login_url='login')
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

    return render(request, 'orden/orden_formulario.html',data)

@login_required(login_url='login')
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

    return render(request, 'orden/orden_formulario.html', data)

@login_required(login_url='login')
def orden_eliminar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    ordenes.delete()
    return redirect(to='orden_listar')

#SEGUIMIENTO====================================================================================
tituloS="Seguimiento"
tituloPluS="Seguimientos"

@login_required(login_url='login')
def seguimiento_listar(request, id):
    listado_all = Seguimiento.objects.all().filter(activo=True, id_orden=id).order_by('-id') 
    orden = get_object_or_404(Orden, id=id)
    filas = 7
    pages = request.GET.get('page',1)    
        
    try:
        paginator = Paginator(listado_all, filas)
        listadoPaginador = paginator.page(pages)
        filaInicio= (filas * listadoPaginador.number) - (filas - 1)

        filasTotales = (filas * listadoPaginador.number)  
        if ( filasTotales < listado_all.count()): 
            filaFin=filasTotales
        else:
            filaFin=listado_all.count()

    except:
        raise Http404

    data={
        'entity':listadoPaginador,
        'paginator':paginator,
        'totalFilas':listado_all.count(),
        'filaInicio': filaInicio,
        'filaFin':filaFin,
        'pageTitulo': tituloS,
        'pageTituloPlu': tituloPluS,
        'pageAccion': 'Listado',
        'orden':orden,
    }
    return render(request, 'orden/seguimiento/seguimiento_listar.html',data)

@login_required(login_url='login')
def seguimiento_agregar(request, idOrden,nombreOrden):
    data = {
        'form': SeguimientoForm(),
        'pageTitulo': tituloS,
        'pageTituloPlu': tituloPluS,
        'pageAccion': 'Agregar',
        'idOrden':idOrden,
        'nombreOrden':nombreOrden,
    }

    if request.method == 'POST':
        formulario = SeguimientoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Seguimiento ingresado correctamente")

            redirect("seguimiento_agregar")
        else:
            data["form"] = formulario
            messages.error(request, 'Problemas para ingresar el seguimiento')

    return render(request, 'orden/seguimiento/seguimiento_formulario.html',data)


@login_required(login_url='login')
def seguimiento_modificar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    data = {
        'form':OrdenesForm(instance=ordenes),
        'pageTitulo': tituloS,
        'pageTituloPlu': tituloPluS,
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

    return render(request, 'orden/seguimiento/seguimiento_formulario.html', data)

@login_required(login_url='login')
def seguimiento_eliminar(request, id):
    ordenes = get_object_or_404(Orden, id=id)
    ordenes.delete()
    return redirect(to='seguimiento_listar')


















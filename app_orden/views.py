from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from app_orden.forms import OrdenesForm, SeguimientoForm,SeguimientoAvanceForm
from django.contrib.auth.decorators import login_required
from .models import Orden, Seguimiento, SeguimientoAvance,SeguimientoAvance
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
        formulario = OrdenesForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.info(request, titulo + ' ingresada correctamente')

            redirect("orden_agregar")
        else:
            data["form"] = formulario
            messages.error(request, 'Problemas para ingresar la ' + titulo)

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
            messages.info(request, titulo + ' modificada correctamente')

            return redirect("orden_modificar",id)
        else:
            messages.error(request, 'Problemas para modificar la ' + titulo)
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
def seguimiento_agregar(request, idOrden):
    orden = get_object_or_404(Orden, id=idOrden)

    data = {
        'form': SeguimientoForm(initial={'id_orden': idOrden}),
        'pageTitulo': tituloS,
        'pageTituloPlu': tituloPluS,
        'pageAccion': 'Agregar',
        'orden':orden,
    }

    if request.method == 'POST':
        form = SeguimientoForm(data=request.POST)

        if form.is_valid():            
            form.save()
            messages.info(request, tituloS + ' ingresado correctamente')

            redirect("orden/seguimiento/seguimiento_agregar")
        else:
            data["form"] = form
            messages.error(request, 'Problemas para ingresar el ' + tituloS)

    return render(request, 'orden/seguimiento/seguimiento_formulario.html',data)

@login_required(login_url='login')
def seguimiento_modificar(request, id):
    seguimientos = get_object_or_404(Seguimiento, id=id)
    orden = get_object_or_404(Orden, nombre=seguimientos.id_orden)

    data = {
        'form':SeguimientoForm(instance=seguimientos),
        'pageTitulo': tituloS,
        'pageTituloPlu': tituloPluS,
        'pageAccion': 'Modificar',
        'orden':orden,
    }

    if request.method == 'POST':
        formulario = SeguimientoForm(data=request.POST, instance=seguimientos)
        if formulario.is_valid():
            formulario.save()
            messages.info(request, tituloS + ' modificado correctamente')

            return redirect("seguimiento_modificar",id)
        else:
            messages.error(request, 'Problemas para modificar el ' + tituloS)
            data["form"] = formulario

    return render(request, 'orden/seguimiento/seguimiento_formulario.html', data)

@login_required(login_url='login')
def seguimiento_eliminar(request, id):
    objeto = get_object_or_404(Seguimiento, id=id)
    orden = get_object_or_404(Orden, nombre=objeto.id_orden)

    objeto.delete()
    return redirect('seguimiento_listar',orden.id)
    
#AVANCE - SEGUIMIENTO ====================================================================================
tituloA="Avance"
tituloPluA="Avances"  

@login_required(login_url='login')
def avance_listar(request, id):
    listado_all = SeguimientoAvance.objects.all().filter(id_seguimiento=id).order_by('-id') 
    seguimiento = get_object_or_404(Seguimiento, id=id)
    orden = get_object_or_404(Orden, nombre=seguimiento.id_orden)
    
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
        'pageTitulo': tituloA,
        'pageTituloPlu': tituloPluA,
        'pageAccion': 'Listado',
        'seguimiento':seguimiento,
        'orden':orden,  
    }
    return render(request, 'orden/seguimiento/avance/avance_listar.html',data)

@login_required(login_url='login')
def avance_agregar(request, idSeguimiento):
    seguimiento = get_object_or_404(Seguimiento, id=idSeguimiento)
    orden = get_object_or_404(Orden, nombre=seguimiento.id_orden)

    data = {
        'form': SeguimientoAvanceForm(initial={'id_seguimiento': idSeguimiento}),
        'pageTitulo': tituloA,
        'pageTituloPlu': tituloPluA,
        'pageAccion': 'Agregar',
        'seguimiento':seguimiento,
        'orden':orden,
    }

    if request.method == 'POST':
        form = SeguimientoAvanceForm(data=request.POST)

        if form.is_valid():            
            form.save()
            messages.info(request, tituloA + ' ingresado correctamente')

            redirect("orden/avance/avance_agregar")
        else:
            data["form"] = form
            messages.error(request, 'Problemas para ingresar el ' + tituloA)

    return render(request, 'orden/seguimiento/avance/avance_formulario.html',data)

@login_required(login_url='login')
def avance_modificar(request, id):
    avance = get_object_or_404(SeguimientoAvance, id=id)
    seguimiento = get_object_or_404(Seguimiento, nombre=avance.id_seguimiento)
    orden = get_object_or_404(Orden, nombre=seguimiento.id_orden)

    data = {
        'form':SeguimientoAvanceForm(instance=avance),
        'pageTitulo': tituloA,
        'pageTituloPlu': tituloPluA,
        'pageAccion': 'Modificar',
        'seguimiento':seguimiento,
        'orden':orden,
    }

    if request.method == 'POST':
        formulario = SeguimientoAvanceForm(data=request.POST, instance=avance)
        if formulario.is_valid():
            formulario.save()
            messages.info(request, tituloA + ' modificado correctamente')

            return redirect("avance_modificar",id)
        else:
            messages.error(request, 'Problemas para modificar el ' + tituloA)
            data["form"] = formulario

    return render(request, 'orden/seguimiento/avance/avance_formulario.html', data)

@login_required(login_url='login')
def avance_eliminar(request, id):
    objeto = get_object_or_404(SeguimientoAvance, id=id)
    seguimiento = get_object_or_404(Seguimiento, nombre=objeto.id_seguimiento)

    objeto.delete()
    return redirect('avance_listar',seguimiento.id)
    
from django.shortcuts import HttpResponse
from django.shortcuts import render

html_base = """
 <h1>Shopping Car</h1>
 <ul>
   <li><a href="/">Inicio</a></li>
   <li><a href="/articulo/">Articulos</a></li>
   <li><a href="/cliente/">Clientes</a></li>
   <li><a href="/venta/">Ventas</a></li>
   <li><a href="/consulta/">Consultas</a></li>
 </li>
"""
def inicio(request):
    data = {
        'titulo':"Inicio"
    }
    return render(request,'base.html',data)


def articulo(request):
  return HttpResponse(html_base+
    """<h2>Mantenimiento de Articulo</h2>
       <p>List de articulos</p>""")

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def cliente(request):
  data = {
      'titulo':'GESTION DE CLIENTES',
      'crear_url': '/crearcliente',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/listCliente.html",data)

def crearCliente(request):
  data = {
      'titulo':'MANTENIMIENTO DE CLIENTES',
      'crear_url':'/crearcliente',
      'action':'add',
      'listar_url': '/cliente',
  }
  return render(request, "ventas/clientes/formCliente.html",data)


def FichaPersonal(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "FichaPersonal/fichaPersonal.html", data)

def empleado(request):
  data = {
      'titulo':'GESTION DE EMPLEADOS',
      'crear_url': '/crearEmpleado',
      'listar_url': '/empleado',
  }
  return render(request, "FichaPersonal/empleados/listEmpleado.html",data)

def crearEmpleado(request):
  data = {
      'titulo':'MANTENIMIENTO DE EMPLEADOS',
      'crear_url':'/crearEmpleado',
      'action':'add',
      'listar_url': '/empleado',
  }
  return render(request, "FichaPersonal/empleados/formEmpleado.html",data)

def eliminarEmpleado(request):
    data = {

    }
    return render(request, "FichaPersonal/empleados/eliminar_empleado.html", data)

def datosMedicos(request):
  data = {
      'titulo':'GESTION DE DATOS MÈDICOS DE EMPLEADOS',
      'crear_url': '/crearDatosMedicos',
      'listar_url': '/datosMedicos',
  }
  return render(request, "FichaPersonal/DatosMedicos/listDatosMedicos.html",data)

def crearDatosMedicos(request):
  data = {
      'titulo':'MANTENIMIENTO DE DATOS MÈDICOS DE EMPLEADOS',
      'crear_url':'/crearDatosMedicos',
      'action':'add',
      'listar_url': '/datosMedicos',
  }
  return render(request, "FichaPersonal/DatosMedicos/formDatosMedico.html",data)

def contactoEmergencias(request):
  data = {
      'titulo':'GESTION DE CONTACTO DE EMERGENCIA DE EMPLEADOS',
      'crear_url': '/crearContactoEmergencias',
      'listar_url': '/contactoEmergencias',
  }
  return render(request, "FichaPersonal/ContactoEmergencia/listContactoEmergencia.html",data)

def crearContactoEmergencias(request):
  data = {
      'titulo':'MANTENIMIENTO DE CONTACTO DE EMERGENCIA DE EMPLEADOS',
      'crear_url':'/crearContactoEmergencias',
      'action':'add',
      'listar_url': '/contactoEmergencias',
  }
  return render(request, "FichaPersonal/ContactoEmergencia/formContactoEmergencia.html",data)

def infoAcademica(request):
  data = {
      'titulo':'GESTION DE INFORMACIÒN ACADÈMICA DE EMPLEADOS',
      'crear_url': '/crearInfoAcademica',
      'listar_url': '/infoAcademica',
  }
  return render(request, "FichaPersonal/InformacionAcademica/listInfoAcademica.html",data)

def crearInfoAcademica(request):
  data = {
      'titulo':'MANTENIMIENTO DE INFORMACIÒN ACADÈMICA DE EMPLEADOS',
      'crear_url':'/crearInfoAcademica',
      'action':'add',
      'listar_url': '/infoAcademica',
  }
  return render(request, "FichaPersonal/InformacionAcademica/formInfoAcademica.html",data)

def capacitaciones(request):
  data = {
      'titulo':'GESTION DE CAPACITACIÒN DE EMPLEADOS',
      'crear_url': '/crearCapacitaciones',
      'listar_url': '/capacitaciones',
  }
  return render(request, "FichaPersonal/Capacitaciones/listCapacitaciones.html",data)

def crearCapacitaciones(request):
  data = {
      'titulo':'MANTENIMIENTO DE CAPACITACIÒN DE EMPLEADOS',
      'crear_url':'/crearCapacitaciones',
      'action':'add',
      'listar_url': '/capacitaciones',
  }
  return render(request, "FichaPersonal/Capacitaciones/formCapacitacion.html",data)

def cargo(request):
  data = {
      'titulo':'CARGOS',
      'crear_url':'/crearCargo',
      'action':'add',
      'listar_url': '/cargo',
  }
  return render(request, "FichaPersonal/cargo/listCargos.html",data)

def crearCargo(request):
  data = {
      'titulo':'MANTENIMIENTO DE CARGOS',
      'crear_url':'/crearCargo',
      'action':'add',
      'listar_url': '/cargo',
  }
  return render(request, "FichaPersonal/cargo/formCargo.html",data)


def eliminarCargo(request):
    data = {

    }
    return render(request, "FichaPersonal/cargo/eliminar_cargo.html",data)

def departamento(request):
  data = {
      'titulo':'DEPARTAMENTOS',
      'crear_url':'/crearDepartamento',
      'action':'add',
      'listar_url': '/departamento',
  }
  return render(request, "FichaPersonal/departamento/listDepartamentos.html",data)

def crearDepartamento(request):
  data = {
      'titulo':'MANTENIMIENTO DE DEPARTAMENTOS',
      'crear_url':'/crearDepartamento',
      'action':'add',
      'listar_url': '/departamento',
  }
  return render(request, "FichaPersonal/departamento/formDepartamento.html",data)


def eliminarDepartamento(request):
    data = {

    }
    return render(request, "FichaPersonal/departamento/eliminar_departamento.html", data)


def sueldo(request):
  data = {
      'titulo':'SUELDOS',
      'crear_url':'/sueldo',
      'action':'add',
      'listar_url': '/sueldo',
  }
  return render(request, "FichaPersonal/sueldo/sueldo.html",data)

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

def venta(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "ventas/ventas.html",data)

def FichaPersonal(request):
  data = {
        'titulo': "Inicio"
  }
  return render(request, "FichaPersonal/fichaPersonal.html", data)

def crearFicha(request):
  data = {
      'titulo':'REGISTRO DE EMPLEADOS',
      'crear_url':'/crearempleado',
      'action':'add',
      'listar_url': '/empleado',
  }
  return render(request, "FichaPersonal/empleados/formEmpleado.html",data)

def cargo(request):
  data = {
      'titulo':'CARGOS',
      'crear_url':'/crearcargo',
      'action':'add',
      'listar_url': '/cargo',
  }
  return render(request, "FichaPersonal/cargo/cargo.html",data)

def departamento(request):
  data = {
      'titulo':'DEPARTAMENTOS',
      'crear_url':'/creardepartamento',
      'action':'add',
      'listar_url': '/departamento',
  }
  return render(request, "FichaPersonal/departamento/departamento.html",data)

def sueldo(request):
  data = {
      'titulo':'SUELDOS',
      'crear_url':'/sueldo',
      'action':'add',
      'listar_url': '/sueldo',
  }
  return render(request, "FichaPersonal/sueldo/sueldo.html",data)

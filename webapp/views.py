from django.shortcuts import render, redirect
from .models import Materiales, Marca, Grupo, Proveedor, Unidad
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import MaterialesForm, GrupoForm, MarcaForm, ProveedorForm, UnidadForm, CreateUserForm
from django.http import HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from django.urls import reverse_lazy




# Create your views here.
#-------------------------------------------------------------------------------------------
# MATERIALES

def inicio(request):
    return render(request, "webapp/index.html")

@login_required(login_url=reverse_lazy("login"))
def materiales(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        materiales_totales = Materiales.objects.filter(Q(descripcion__icontains=search_post))
        paginator = Paginator(materiales_totales, 15)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        materiales_totales = Materiales.objects.all().order_by("-fecha_precio")
        paginator = Paginator(materiales_totales,15)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "materiales/listar.html", {
        "paginas": paginas,

    })

@login_required(login_url=reverse_lazy("login"))
def eliminar(request, id):
    material = Materiales.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        material.delete()
        # redirect to the bands list
        return redirect('listar-materiales')
    return render(request,
                    'materiales/confirm_delete.html',
                    {'material': material})

@login_required(login_url=reverse_lazy("login"))
def crearMaterial(request):
    formulario = MaterialesForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "materiales/crear.html", {
        "formulario":formulario    
    })


@login_required(login_url=reverse_lazy("login"))
def confirm_create(request):
    return render(request, "materiales/confirm_create.html")
@login_required(login_url=reverse_lazy("login"))
def confirm_edit(request):
    return render(request, "materiales/confirm_edit.html")

@login_required(login_url=reverse_lazy("login"))
def editar_material(request, id):
    material = Materiales.objects.get(id=id)
    formulario = MaterialesForm(request.POST or None, instance=material)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return HttpResponseRedirect("confirm-edit")
    return render(request, "materiales/editar.html", {"formulario" : formulario})

#-------------------------------------------------------------------------------------------------------------------------------
# GRUPO

@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def listar_grupo(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        grupo_totales = Grupo.objects.filter(Q(categoria__icontains=search_post))
        paginator = Paginator(grupo_totales, 10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        grupo_totales = Grupo.objects.all().order_by("-categoria")
        paginator = Paginator(grupo_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "grupo/listar.html", {
        "paginas": paginas,

    })

@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def eliminar_grupo(request, id):
    grupo = Grupo.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            grupo.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-grupo')
    return render(request,
                    'grupo/confirm_delete.html',
                    {'grupo': grupo})
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def cant_erase(request):
    return render(request, "grupo/cannot_erase.html")
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def crearGrupo(request):
    formulario_gr = GrupoForm(request.POST or None)
    if formulario_gr.is_valid():
        formulario_gr.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "grupo/crear.html", {
        "formulario":formulario_gr    
    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def confirm_create_gr(request):
    return render(request, "grupo/confirm_create.html")

#-------------------------------------------------------------------------------------------------------------------------------
# MARCA

@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def listar_marca(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        marca_totales = Marca.objects.filter(Q(nombre__icontains=search_post))
        paginator = Paginator(marca_totales, 15)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        marca_totales = Marca.objects.all().order_by("-nombre")
        paginator = Paginator(marca_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "marca/listar.html", {
        "paginas": paginas,

    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def crearMarca(request):
    formulario_mrk = MarcaForm(request.POST or None)
    if formulario_mrk.is_valid():
        formulario_mrk.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "marca/crear.html", {
        "formulario":formulario_mrk    
    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def confirm_create_mkr(request):
    return render(request, "marca/confirm_create.html")

@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def eliminar_marca(request, id):
    marca = Marca.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            marca.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-marca')
    return render(request,
                    'marca/confirm_delete.html',
                    {'marca': marca})

@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def cant_erase_mk(request):
    return render(request, "marca/cannot_erase.html")

#-------------------------------------------------------------------------------------------------------------------------------
# PROVEEDOR
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def listar_proveedor(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        proveedor_totales = Proveedor.objects.filter(Q(nombre__icontains=search_post))
        paginator = Paginator(proveedor_totales, 5)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        proveedor_totales = Proveedor.objects.all().order_by("-nombre")
        paginator = Paginator(proveedor_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "proveedor/listar.html", {
        "paginas": paginas,

    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def crearProveedor(request):
    formulario_prvd = ProveedorForm(request.POST or None)
    if formulario_prvd.is_valid():
        formulario_prvd.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "proveedor/crear.html", {
        "formulario":formulario_prvd 

    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def confirm_create_prvd(request):
    return render(request, "proveedor/confirm_create.html")
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def editar_proveedor(request, id):
    material = Proveedor.objects.get(id=id)
    formulario = ProveedorForm(request.POST or None, instance=material)
    if formulario.is_valid() and request.method == "POST":
        formulario.save()
        return HttpResponseRedirect("confirm-edit-prv")
    return render(request, "proveedor/editar.html", {"formulario" : formulario})
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def confirm_edit_prv(request):
    return render(request, "proveedor/confirm_edit.html")


@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def eliminar_proveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            proveedor.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-proveedor')
    return render(request,
                    'proveedor/confirm_delete.html',
                    {'proveedor': proveedor})


#-------------------------------------------------------------------------------------------------------------------------------
# UNIDADES

@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")

def listar_unidades(request):

    search_post = request.GET.get('search')
    print(search_post)

    if search_post:

        unidad_totales = Unidad.objects.filter(Q(unidad__icontains=search_post))
        paginator = Paginator(unidad_totales, 10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        

    else:
        # If not searched, return default posts
        unidad_totales = Unidad.objects.all().order_by("-unidad")
        paginator = Paginator(unidad_totales,10)
        page = request.GET.get('page')
        paginas = paginator.get_page(page)
        paginas.adjusted_elided_pages = paginator.get_elided_page_range(page)
        
        
        #marcas= Marca.objects.all()
    return render(request, "unidades/listar.html", {
        "paginas": paginas,

    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def eliminar_unidad(request, id):
    unidad = Unidad.objects.get(id=id)  # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        try:
            unidad.delete()
        except ProtectedError:
        # redirect to the bands list
            return HttpResponseRedirect("cant-erase")
            
        
        
        return redirect('listar-unidades')
    return render(request,
                    'unidades/confirm_delete.html',
                    {'unidad': unidad})
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def cant_erase(request):
    return render(request, "unidades/cannot_erase.html")
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def crearUnidades(request):
    formulario_und = UnidadForm(request.POST or None)
    if formulario_und.is_valid():
        formulario_und.save()
        return HttpResponseRedirect("confirm-create")
    
    return render(request, "unidades/crear.html", {
        "formulario_und":formulario_und
    })
@login_required(login_url=reverse_lazy("login"))
@staff_member_required(login_url="relogin")
def confirm_create_und(request):
    return render(request, "unidades/confirm_create.html")


#-------------------------------------------------------------------------------------------------------------------------------
# REGISTRO



def registerPage(request): # https://github.com/KenBroTech/Django-Inventory-Management-System/blob/master/user/views.py
                        # https://www.youtube.com/watch?v=UJehAE0GMEI
    formulario_reg= CreateUserForm(request.POST or None)
    if formulario_reg.is_valid():
        formulario_reg.save()
        return HttpResponseRedirect("registration/confirm-create")
    
    return render(request, "registration/register.html", {
        "formulario_reg":formulario_reg
    })

def confirm_create_reg(request):
    return render(request, "registration/confirm_create.html")

   
def login_view(request):

    if request.method == "POST":

        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = CustomAuthenticationForm(request)
    context = {
        "form": form
    }
    return render(request, "registration/login.html", context)
    

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    return render(request, "registration/logout.html", {})

def relogin_view(request):
    return render(request, "registration/relogin.html")
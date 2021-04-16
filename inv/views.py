from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from bases.views import sin_privilegios


from django.contrib.auth.decorators import login_required,permission_required

from .models import Categoria,SubCategoria,Marca,UnidadMedida,Producto,historiareporte
from .forms import CategoriaForm,SubCategoriaForm,MarcaForm,UMForm,ProductoForm,precisionForm
from openpyxl import Workbook
from django.http.response import HttpResponse

# Create your views here.

# creacion de los view de la categoria
class CategoriaView(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_categoria"
    model=Categoria
    template_name="inv/categoria_list.html"
    context_object_name="obj"
    login_url="bases:login"
class CategoriaNew(LoginRequiredMixin,sin_privilegios,generic.CreateView):
    permission_required="inv.view_categoria"
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name="obj"
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url="bases:login"
    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin,sin_privilegios,generic.UpdateView,):
    permission_required="inv.view_categoria"
    model=Categoria
    template_name="inv/categoria_form.html"
    context_object_name="obj"   
    form_class=CategoriaForm
    success_url=reverse_lazy("inv:categoria_list")
    login_url="bases:login" 
    
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)

# class CategoriaDel(LoginRequiredMixin,generic.DeleteView):
#     model=Categoria
#     template_name='inv/categoria_del.html'
#     context_object_name='obj'
#     success_url=reverse_lazy("inv:categoria_list")

@login_required(login_url='/login/')
@permission_required('inv.change_catalogo',login_url='bases:sin_privilegios')

def categoria_inactivar(request,id):
    cat=Categoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"

    if not cat:
        return redirect("inv:categoria_list")
    if request.method=='GET':
        contexto={'obj':cat}
    if request.method=='POST':
        cat.estado=False
        cat.save()
        return redirect("inv:categoria_list")
    return render(request,template_name,contexto)




# creacion de las view de la subCategoria
class SubCategoriaView(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_subcategoria"
    model=SubCategoria
    template_name="inv/subcategoria_list.html"
    context_object_name="obj"
    login_url="bases:login"
class SubCategoriaNew(LoginRequiredMixin,sin_privilegios,generic.CreateView):
    permission_required="inv.view_subcategoria"
    model=SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name="obj"
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url="bases:login"
    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class SubCategoriaEdit(LoginRequiredMixin,sin_privilegios,generic.UpdateView):
    permission_required="inv.view_subcategoria"
    model=SubCategoria
    template_name="inv/subcategoria_form.html"
    context_object_name="obj"   
    form_class=SubCategoriaForm
    success_url=reverse_lazy("inv:subcategoria_list")
    login_url="bases:login" 
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)
# class SubCategoriaDel(LoginRequiredMixin,generic.DeleteView):
#     model=SubCategoria
#     template_name='inv/subcategoria_del.html'
#     context_object_name='obj'
#     success_url=reverse_lazy("inv:subcategoria_list")
@login_required(login_url='/login/')
@permission_required('inv.change_subcategoria',login_url='bases:sin_privilegios')

def sub_inactivar(request,id):
    sub=SubCategoria.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"

    if not sub:
        return redirect("inv:subcategoria_list")
    if request.method=='GET':
        contexto={'obj':sub}
    if request.method=='POST':
        sub.estado=False
        sub.save()
        return redirect("inv:subcategoria_list")
    return render(request,template_name,contexto)




# creacion de los view de la marca

class MarcaView(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_marca"
    model=Marca
    template_name="inv/marca_list.html"
    context_object_name="obj"
    login_url="bases:login"
    permission_required="inv.view_marca"

class MarcaNew(LoginRequiredMixin,sin_privilegios,generic.CreateView):
    permission_required="inv.view_marca"
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name="obj"
    form_class=MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    login_url="bases:login"

    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin,sin_privilegios,generic.UpdateView):
    permission_required="inv.view_marca"
    model=Marca
    template_name="inv/marca_form.html"
    context_object_name="obj"   
    form_class=MarcaForm
    success_url=reverse_lazy("inv:marca_list")
    login_url="bases:login" 
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)
@login_required(login_url='/login/')
@permission_required('inv.change_marca',login_url='bases:sin_privilegios')
def marca_inactivar(request,id):
    marca =Marca.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"


    if not marca:
        return redirect("inv:marca_list")
    if request.method=='GET':
        contexto={'obj':marca}
    if request.method=='POST':
        marca.estado=False
        marca.save()
        return redirect("inv:marca_list")


    return render(request,template_name,contexto)


#----------------------- creacion de las unidades de medida--------------




class UMView(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_unidadmedida"
    model=UnidadMedida
    template_name="inv/um_list.html"
    context_object_name="obj"
    login_url="bases:login"

class UMNew(LoginRequiredMixin,sin_privilegios,generic.CreateView):
    permission_required="inv.view_unidadmedida"
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name="obj"
    form_class=UMForm
    success_url=reverse_lazy("inv:um_list")
    login_url="bases:login"

    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)

class UMEdit(LoginRequiredMixin,sin_privilegios,generic.UpdateView):
    permission_required="inv.view_unidadmedida"
    model=UnidadMedida
    template_name="inv/um_form.html"
    context_object_name="obj"   
    form_class=UMForm
    success_url=reverse_lazy("inv:um_list")
    login_url="bases:login" 
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)

def um_inactivar(request,id):
    um =UnidadMedida.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"


    if not um:
        return redirect("inv:um_list")
    if request.method=='GET':
        contexto={'obj':um}
    if request.method=='POST':
        um.estado=False
        um.save()
        return redirect("inv:um_list")


    return render(request,template_name,contexto)

    #--------------creacion delos view de productos
class ProductoView(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_producto"
    model=Producto
    template_name="inv/producto_list.html"
    context_object_name='obj'
    login_url="bases:login"

class ProductoNew(LoginRequiredMixin,sin_privilegios,generic.CreateView):
    permission_required="inv.view_producto"
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name="obj"
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url="bases:login"

    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class ProductoEdit(LoginRequiredMixin,sin_privilegios,generic.UpdateView):
    permission_required="inv.view_producto"
    model=Producto
    template_name="inv/producto_form.html"
    context_object_name='obj'
    form_class=ProductoForm
    success_url=reverse_lazy("inv:producto_list")
    login_url="bases:login"
    
    def form_valid(self,form):
        form.instance.um=self.request.user.id
        return super().form_valid(form)


def producto_inactivar(request,id):
    prod=Producto.objects.filter(pk=id).first()
    contexto={}
    template_name="inv/catalogo_del.html"

    if not prod:
        return redirect("inv:producto_list")
    if request.method=='GET':
        contexto={'obj':prod}
    if request.method=='POST':
        prod.estado=False
        prod.save()
        return redirect("inv:producto_list")
    return render(request,template_name,contexto)



class reporteprecisionView(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_producto"
    model=Producto
    template_name="inv/reporte_preci.html"
    context_object_name="obj"
    login_url="bases:login"

class guardarprecision(LoginRequiredMixin,sin_privilegios,generic.CreateView):
    permission_required="inv.view_categoria"
    model=Producto
    template_name="inv/guardar_precision.html"
    context_object_name="obj"
    login_url="bases:login"
    form_class=precisionForm
    success_url=reverse_lazy("inv:precision_lista")
    login_url="bases:login"
    def form_valid(self,form):
        form.instance.uc=self.request.user
        return super().form_valid(form)
class precisionlist(LoginRequiredMixin,sin_privilegios,generic.ListView):
    permission_required="inv.view_producto"
    model=historiareporte
    template_name="inv/precision_list.html"
    context_object_name="obj"
    login_url="bases:login"



# class reporte_excel(LoginRequiredMixin,sin_privilegios,generic.ListView):
#     def get(self,request,*arg,**kwargs):
#         productos=Producto.objects.all()
#         wb=Workbook()
#         ws = wb.active




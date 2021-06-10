from django.urls import path
from .views import CategoriaView,CategoriaNew,CategoriaEdit, \
    categoria_inactivar , \
        SubCategoriaView,SubCategoriaNew,SubCategoriaEdit,sub_inactivar,MarcaView,MarcaNew,MarcaEdit,marca_inactivar,UMView,UMNew,UMEdit,um_inactivar,ProductoView,ProductoEdit,ProductoNew,producto_inactivar,reporteprecisionView,guardarprecision,precisionlist,reporte_excel
from .reportes import producto_total
urlpatterns=[
    #RUTAS DE LAS CATEGORIAS
    path('categorias/',CategoriaView.as_view(),name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(),name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(),name='categoria_edit'),
    path('categorias/inactivar/<int:id>',categoria_inactivar,name='categoria_inactivar'),
    
    #RUTAS DE LAS SUBCATEGORIAS
    
    path('subcategorias/',SubCategoriaView.as_view(),name='subcategoria_list'),
    path('subcategorias/new',SubCategoriaNew.as_view(),name='subcategoria_new'),
    path('subcategorias/edit/<int:pk>',SubCategoriaEdit.as_view(),name='subcategoria_edit'),
    path('subcategorias/inactivar/<int:id>',sub_inactivar,name='subcategoria_inactivar'),

    #RUTAS DE LAS MARCAS
    path('marcas/',MarcaView.as_view(),name='marca_list'),
    path('marcas/new',MarcaNew.as_view(),name='marca_new'),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(),name='marca_edit'),
    path('marcas/inactivar/<int:id>',marca_inactivar,name='marca_inactivar'),


    #RUTAS DE LAS UNIDADES DE MEDIDA
    path('um/',UMView.as_view(),name='um_list'),
    path('um/new',UMNew.as_view(),name='um_new'),
    path('um/edit/<int:pk>',UMEdit.as_view(),name='um_edit'),
    path('um/inactivar/<int:id>',um_inactivar,name='um_inactivar'),
    

    #RUTAS DE LOS PRODUCTOS 
    path('productos/',ProductoView.as_view(),name='producto_list'),
    path('productos/new',ProductoNew.as_view(),name='producto_new'),
    path('productos/edit/<int:pk>',ProductoEdit.as_view(),name='producto_edit'),
    path('productos/inactivar/<int:id>',producto_inactivar,name='producto_inactivar'),
    path('productos/precision',reporteprecisionView.as_view(),name='reporte_preci'),
    path('productos/precision/guardar',guardarprecision.as_view(),name='guardar_preci'),
    path('productos/precision/listado',precisionlist.as_view(),name='precision_lista'),
    
    # path('categorias/new',CategoriaNew.as_view(),name='categoria_new'),
    # path('categorias/edit/<int:pk>',CategoriaEdit.as_view(),name='categoria_edit'),

    
    
    path('productos/listado',producto_total,name='productos_print'),
    #excel
    path('reporteproductoexcel',reporte_excel.as_view(),name='reporteexcelproducto'),
    


]
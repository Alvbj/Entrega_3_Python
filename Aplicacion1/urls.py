from django.urls import path
from Aplicacion1.views import vista_cliente, vista_inicio, vista_proveedor, vista_producto

urlpatterns = [
    
    path('urlinicio/',vista_inicio,name="inicio"),
    path('urlcliente/',vista_cliente,name="cliente"),
    path('urlproveedor/',vista_proveedor,name="proveedor"),
    path('urlproducto/',vista_producto,name="producto"),
]
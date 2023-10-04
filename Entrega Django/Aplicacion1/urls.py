from django.urls import path
from Aplicacion1.views import inicio, crear_cliente, alta_proveedor,prod

urlpatterns = [
    path("",inicio,name="Inicio"),
    path("crear-usuario/<str:nombre>/<str:razon_social>",crear_cliente,name="Crear Cliente"), #Con esto, los  valores que le pase en el link me los toma como escritos
    path("crear-proveedor/<str:proveedor>/<str:tipo>",alta_proveedor,name="Crear Proveedor"), #Con esto, los  valores que le pase en el link me los toma como escritos
    path("productos/<str:producto>/<str:subrubro>/<str:rubro>",prod,name="Productos"), #Con esto, los  valores que le pase en el link me los toma como escritos
]
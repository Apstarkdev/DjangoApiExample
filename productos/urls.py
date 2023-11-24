from django.urls import path
from .views import ProductoLista, ProductoDetalle

urlpatterns = [
    path('productos/', ProductoLista.as_view(), name='producto-lista'),
    path('productos/<int:pk>/', ProductoDetalle.as_view(), name='producto-detalle'),
]
from django.urls import path
from .views import ListaLibrosView, DetallesLibroView, CrearLibroView, TomarPrestadoDevolverLibroView, LibrosPrestadosEntregadosView, signin, cerrar, error_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

handler404 = 'biblioteca.views.error_404'

urlpatterns = [
  path('<path>', error_404, name='404'),
  path('', signin, name='login'),
  path('logout/', cerrar, name='logout'),
  path('libros/', ListaLibrosView.as_view(), name='lista_libros'),
  path('libros/<int:pk>/', DetallesLibroView.as_view(), name='detalles_libro'),
  path('libros/nuevo/', CrearLibroView.as_view(), name='crear_libro'),
  path('tomar-devolver-libro/', TomarPrestadoDevolverLibroView.as_view(), name='tomar_devolver_libro'),
  path('libros-prestados-entregados/', LibrosPrestadosEntregadosView.as_view(), name='libros_prestados_entregados'),
]
# Create your views here.
from django import forms
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login, logout
from .models import Libro
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Vista para el inicio de sesión
def signin(request):
    # Si la solicitud es GET, muestra el formulario de inicio de sesión
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        # Si la solicitud es POST, intenta autenticar al usuario
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, username=username, password=password)
        
        # Si el usuario no está autenticado, muestra un mensaje de error
        if user is None: 
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Error en usuario o contraseña'
            })
        else:
            # Si el usuario está autenticado, inicia sesión y redirige a la página de lista de libros
            login(request, user)
            return redirect('lista_libros')

# Vista para cerrar sesión
def cerrar(request):
    logout(request)
    return redirect('/')

# Vista personalizada para manejar errores 404
def error_404(request, exception):
    return render(request, '404.html', status=404)

# Vista basada en clase para listar libros (requiere inicio de sesión)
class ListaLibrosView(LoginRequiredMixin, ListView):
    model = Libro
    template_name = 'lista_libros.html'
    context_object_name = 'libros'
    login_url = 'login'
    redirect_field_name = 'login'

# Vista basada en clase para mostrar los detalles de un libro (requiere inicio de sesión)
class DetallesLibroView(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = 'detalles_libro.html'
    login_url = 'login'
    context_object_name = 'libro'

# Vista basada en clase para crear un libro (requiere inicio de sesión como administrador)
class CrearLibroView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Libro
    fields = ['titulo', 'autor', 'año_publi', 'stock']
    login_url = 'login'
    template_name = 'crear_libro.html'
    
    def form_valid(self, form):
        # Guarda el objeto del formulario y muestra un mensaje de éxito
        self.object = form.save()
        messages.success(self.request, '¡El libro se ha creado con éxito!')
        # Crea un nuevo formulario vacío y renderiza la página
        form = self.get_form_class()()
        return self.render_to_response(self.get_context_data(form=form))
    
    def test_func(self):
        # Verifica si el usuario tiene el rol de administrador para acceder a esta vista
        return self.request.user.rol == 'administrador'

# Vista basada en clase para tomar prestado o devolver un libro (requiere inicio de sesión como usuario regular)
class TomarPrestadoDevolverLibroView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        # Verifica si el usuario tiene el rol de usuario regular para acceder a esta vista
        return self.request.user.rol == 'usuario regular'

    def get(self, request):
        # Lógica para tomar prestado y devolver libros aquí
        return render(request, 'tomar_prestado_devolver_libro.html')

# Vista basada en clase para listar libros prestados y entregados (requiere inicio de sesión como usuario regular)
class LibrosPrestadosEntregadosView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        # Verifica si el usuario tiene el rol de usuario regular para acceder a esta vista
        return self.request.user.rol == 'usuario regular'

    def get(self, request):
        # Lógica para listar libros prestados y entregados aquí
        return render(request, 'libros_prestados_entregados.html')
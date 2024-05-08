# Prueba-de-Desarrollador-de-Software-Django
Prueba de Desarrollador de Software Django

# Instrucciones para probar la aplicación

Para probar esta aplicación, sigue los pasos a continuación:

## 1. Descarga el repositorio

Descarga el repositorio.

## 2. Ejecuta el servidor

Abre una terminal y navega hasta el directorio raíz del proyecto. Luego, ejecuta el siguiente comando para iniciar el servidor local:

python manage.py runserver


## 3. Accede a la aplicación

Una vez que el servidor esté en funcionamiento, abre un navegador web y accede a la aplicación ingresando la siguiente URL en la barra de direcciones:

http://localhost:8000/

## 4. Inicia sesión

Para ingresar a la aplicación, es necesario iniciar sesión. Utiliza las siguientes credenciales de prueba:

- **Usuario:** Jose (Administrador)
- **Contraseña:** Jose2552

- **Usuario:** LOPEZ (Usuario Regular)
- **Contraseña:** Jose2552

## 5. Navegación en la barra de navegación

La aplicación cuenta con una barra de navegación que muestra opciones diferentes según el tipo de usuario:

- Para el usuario administrador (Jose):
  - Libros
  - Cerrar Sesión
  - Agregar Libro

- Para el usuario regular (LOPEZ):
  - Libros
  - Cerrar Sesión
  - Prestar/Devolver
  - Mi Historial

## 6. Rutas protegidas

Algunas rutas de la aplicación están protegidas y requieren que el usuario esté autenticado y tenga los permisos adecuados para acceder a ellas. Si intentas acceder a estas rutas sin iniciar sesión, serás redirigido a la página de inicio de sesión.

¡Disfruta explorando la aplicación!

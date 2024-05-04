Libro.__init__(self, titulo, autor, año_publicacion):
Este método inicializa un objeto Libro con un título, autor y año de publicación proporcionados.
Biblioteca.agregar_libro(self, libro):
Agrega un libro a la biblioteca, verificando que tenga un título y autor, y luego lo añade a la lista de libros.
Biblioteca.buscar_libro(self, titulo):
Busca un libro por su título en la biblioteca y devuelve el libro si lo encuentra; de lo contrario, lanza una excepción.
Biblioteca.mostrar_libros(self):
Muestra todos los libros de la biblioteca, incluyendo título, autor y año de publicación, o indica si la biblioteca está vacía.
ErrorLibroSinTitulo(Exception):
Una excepción personalizada que se lanza cuando se intenta agregar un libro sin título.
ErrorLibroSinAutor(Exception):
Una excepción personalizada que se lanza cuando se intenta agregar un libro sin autor.
main():
La función principal del programa que proporciona un menú de opciones para agregar libros, buscar libros por título, mostrar todos los libros y salir del programa.

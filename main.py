from libro import Libro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Buscar libro por título")
        print("3. Mostrar todos los libros")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                año_publicacion = input("Ingrese el año de publicación del libro: ")

                if not titulo:
                    raise ValueError("El libro debe tener un título.")
                if not autor:
                    raise ValueError("El libro debe tener un autor.")

                libro = Libro(titulo, autor, año_publicacion)
                biblioteca.agregar_libro(libro)

            elif opcion == "2":
                titulo = input("Ingrese el título del libro a buscar: ")
                libro_encontrado = biblioteca.buscar_libro(titulo)
                print(f"Libro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")

            elif opcion == "3":
                biblioteca.mostrar_libros()

            elif opcion == "4":
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
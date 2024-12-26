# Listas globales para libros
libros_disponibles = []
libros_prestados = []

def agregar_libro(id, titulo, autor):
    """
    Agrega un libro a la lista de libros disponibles.
    """
    libro = {"id": id, "titulo": titulo, "autor": autor, "estado": "Disponible"}
    libros_disponibles.append(libro)
    print(f"Libro '{titulo}' agregado exitosamente.")

def prestar_libro(id, usuario):
    """
    Presta un libro a un usuario y lo mueve a la lista de libros prestados.
    """
    for libro in libros_disponibles:
        if libro["id"] == id:
            libro["estado"] = "Prestado"
            libro["usuario"] = usuario
            libros_prestados.append(libro)
            libros_disponibles.remove(libro)
            print(f"Libro '{libro['titulo']}' prestado a {usuario}.")
            return
    print("Libro no encontrado o ya prestado.")

def devolver_libro(id):
    """
    Devuelve un libro a la lista de libros disponibles.
    """
    for libro in libros_prestados:
        if libro["id"] == id:
            libro["estado"] = "Disponible"
            libro.pop("usuario", None)
            libros_disponibles.append(libro)
            libros_prestados.remove(libro)
            print(f"Libro '{libro['titulo']}' devuelto exitosamente.")
            return
    print("Libro no encontrado en los libros prestados.")

def buscar_libro_por_titulo(titulo):
    """
    Busca un libro por título y devuelve su información si existe.
    """
    for libro in libros_disponibles + libros_prestados:
        if libro["titulo"].lower() == titulo.lower():
            return libro
    print("Libro no encontrado.")
    return None

def mostrar_libros_disponibles():
    """
    Muestra todos los libros disponibles.
    """
    if libros_disponibles:
        print("\nLibros disponibles:")
        for libro in libros_disponibles:
            print(f"{libro['id']}: {libro['titulo']} - {libro['autor']}")
    else:
        print("\nNo hay libros disponibles.")

def mostrar_libros_prestados():
    """
    Muestra todos los libros prestados con el usuario correspondiente.
    """
    if libros_prestados:
        print("\nLibros prestados:")
        for libro in libros_prestados:
            print(f"{libro['id']}: {libro['titulo']} - {libro['autor']} (Prestado a {libro['usuario']})")
    else:
        print("\nNo hay libros prestados.")

def menu():
    """
    Menú interactivo para la gestión de la biblioteca virtual.
    """
    while True:
        print("\n--- Menú Biblioteca Virtual ---")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Buscar libro por título")
        print("5. Mostrar libros disponibles")
        print("6. Mostrar libros prestados")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del libro: ")
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            agregar_libro(id, titulo, autor)

        elif opcion == "2":
            id = input("Ingrese el ID del libro a prestar: ")
            usuario = input("Ingrese el nombre del usuario: ")
            prestar_libro(id, usuario)

        elif opcion == "3":
            id = input("Ingrese el ID del libro a devolver: ")
            devolver_libro(id)

        elif opcion == "4":
            titulo = input("Ingrese el título del libro a buscar: ")
            libro = buscar_libro_por_titulo(titulo)
            if libro:
                print(f"\nLibro encontrado: {libro}")

        elif opcion == "5":
            mostrar_libros_disponibles()

        elif opcion == "6":
            mostrar_libros_prestados()

        elif opcion == "7":
            print("\nSaliendo del sistema de Biblioteca Virtual. ¡Hasta luego!")
            break

        else:
            print("\nOpción no válida. Por favor, intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()

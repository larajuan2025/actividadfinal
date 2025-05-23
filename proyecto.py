import sqlite3

# Conexión y creación de la base de datos
conexion = sqlite3.connect("peliculas.db")
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS peliculas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        director TEXT,
        año NUMERIC,
    )
''')
conexion.commit()

# Función para agregar una nueva película
def agregar_pelicula():
    titulo = input("Título de la película: ")
    director = input("Director de la película: ")
    año = int(input("Año de estreno: "))
    cursor.execute("INSERT INTO peliculas (titulo, director, anio) VALUES (?, ?, ?)", (titulo, director, año))
    conexion.commit()
    print("Película agregada correctamente.")

# Función para modificar una película
def modificar_pelicula():
    id_pelicula = int(input("ID de la película a modificar: "))
    nuevo_titulo = input("Nuevo título: ")
    nuevo_director = input("Nuevo director: ")
    nuevo_anio = int(input("Nuevo año de estreno: "))
    cursor.execute("UPDATE peliculas SET titulo=?, director=?, anio=? WHERE id=?", (nuevo_titulo, nuevo_director, nuevo_anio, id_pelicula))
    conexion.commit()
    print("Película modificada correctamente.")

# Función para mostrar todas las películas
def mostrar_peliculas():
    cursor.execute("SELECT * FROM peliculas")
    registros = cursor.fetchall()
    if registros:
        for pelicula in registros:
            print(pelicula)
    else:
        print("No hay películas registradas.")

# Función para eliminar una película por ID
def eliminar_pelicula():
    id_pelicula = int(input("ID de la película a eliminar: "))
    cursor.execute("DELETE FROM peliculas WHERE id=?", (id_pelicula,))
    conexion.commit()
    print("Película eliminada correctamente.")

# Función para buscar una película por título
def buscar_pelicula():
    titulo = input("Ingrese el título a buscar: ")
    cursor.execute("SELECT * FROM peliculas WHERE titulo LIKE ?", ('%' + titulo + '%',))
    registros = cursor.fetchall()
    if registros:
        for pelicula in registros:
            print(pelicula)
    else:
        print("No se encontró ninguna película con ese título.")

# Menú con match
def menu():
    while True:
        print("\n--- MENÚ DE OPCIONES ---")
        print("1. Agregar película")
        print("2. Modificar película")
        print("3. Mostrar películas")
        print("4. Eliminar película")
        print("5. Buscar película")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "1":
                agregar_pelicula()
            case "2":
                modificar_pelicula()
            case "3":
                mostrar_peliculas()
            case "4":
                eliminar_pelicula()
            case "5":
                buscar_pelicula()
            case "6":
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")

menu()

# Cerrar conexión al finalizar
conexion.close()
# arreglos.py
albums = []


def agregar_album():
    print("\n--- Agregar un álbum al sistema ---")
    nombre = input("Nombre del álbum: ")
    artista = input("Nombre del artista: ")

    while True:
        try:
            precio = float(input("Precio del álbum: "))
            if precio < 0:
                print("El precio no puede ser negativo. Por favor ingresa un valor válido.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")

    album = {
        "nombre": nombre,
        "artista": artista,
        "precio": precio
    }
    albums.append(album)
    print("Álbum agregado al sistema.")


def mostrar_albumes():
    if not albums:
        print("\nNo hay álbumes registrados.")
    else:
        print("\n--- Álbumes Registrados ---")
        for album in albums:
            print(f"{album['nombre']} - {album['artista']} - ${album['precio']}")


def eliminar_album():
    if albums:
        nombre = input("Introduce el nombre del álbum a eliminar: ")
        for album in albums:
            if album["nombre"] == nombre:
                albums.remove(album)
                print(f"Álbum '{nombre}' eliminado.")
                return
        print(f"\nÁlbum '{nombre}' no encontrado.")
    else:
        print("\nNo hay álbumes para eliminar.")


def menu_arreglos():
    while True:
        print("\n--- Menú de Álbumes (Arreglos) ---")
        print("1. Agregar álbum")
        print("2. Mostrar álbumes")
        print("3. Eliminar álbum")
        print("4. Regresar al Menú Principal")
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            agregar_album()
        elif opcion == '2':
            mostrar_albumes()
        elif opcion == '3':
            eliminar_album()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

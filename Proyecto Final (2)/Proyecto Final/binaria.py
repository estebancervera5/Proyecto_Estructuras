#Busqueda binaria
albumes = [
        {"nombre": "Album A", "artista": "Artista 1", "precio": 10.0},
        {"nombre": "Album B", "artista": "Artista 2", "precio": 15.0},
        {"nombre": "Album C", "artista": "Artista 3", "precio": 20.0},
        {"nombre": "Album D", "artista": "Artista 4", "precio": 25.0},
        {"nombre": "Album E", "artista": "Artista 5", "precio": 30.0},
        {"nombre": "Album F", "artista": "Artista 6", "precio": 35.0},
        {"nombre": "Album G", "artista": "Artista 7", "precio": 40.0},
        {"nombre": "Album H", "artista": "Artista 8", "precio": 45.0},
        {"nombre": "Album I", "artista": "Artista 9", "precio": 50.0},
        {"nombre": "Album J", "artista": "Artista 10", "precio": 55.0}
    ]


    # Función para mostrar los álbumes
def mostrar_albumes():
        print("\nLista de Álbumes:")
        for album in albumes:
            print(f"Nombre: {album['nombre']} | Artista: {album['artista']} | Precio: ${album['precio']:.2f}")


    # Función para realizar búsqueda binaria
def busqueda_binaria(array, precio_buscado):
        inicio = 0
        fin = len(array) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            if array[medio]['precio'] == precio_buscado:
                return medio
            elif array[medio]['precio'] < precio_buscado:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1


    # Menú para gestionar la búsqueda binaria
def menu_busqueda():
        while True:
            print("\n--- Menú de Búsqueda Binaria ---")
            print("1. Ver álbumes")
            print("2. Buscar álbum por precio")
            print("3. Regresar al menú principal")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                mostrar_albumes()
            elif opcion == '2':
                while True:
                    try:
                        precio = float(input("Ingrese el precio del álbum que desea buscar: "))
                        break
                    except ValueError:
                        print("Error: Ingresa un número válido.")

                indice = busqueda_binaria(albumes, precio)
                if indice != -1:
                    album = albumes[indice]
                    print(
                        f"Álbum encontrado: Nombre: {album['nombre']} | Artista: {album['artista']} | Precio: ${album['precio']:.2f}")
                else:
                    print("Álbum no encontrado.")
            elif opcion == '3':
                break
            else:
                print("Opción no válida.")

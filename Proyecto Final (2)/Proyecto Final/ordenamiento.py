#quicksort
albumes = []


# Función para agregar álbumes
def agregar_album():
    nombre = input("Ingrese el nombre del álbum: ")
    artista = input("Ingrese el nombre del artista: ")

    # Validar que el precio sea un número
    while True:
        try:
            precio = float(input("Ingrese el precio del álbum (solo números): "))
            break
        except ValueError:
            print("Error: Debes ingresar un número válido para el precio.")

    albumes.append({'nombre': nombre, 'artista': artista, 'precio': precio})
    print("Álbum agregado con éxito.")


# Función para mostrar álbumes
def mostrar_albumes():
    if not albumes:
        print("\nNo hay álbumes en el sistema.")
    else:
        print("\nLista de Álbumes:")
        for album in albumes:
            print(f"Nombre: {album['nombre']} | Artista: {album['artista']} | Precio: ${album['precio']:.2f}")


# Función de partición para QuickSort
def partition(array, primero, ultimo):
    pivot = array[ultimo]['precio']
    i = primero - 1
    for j in range(primero, ultimo):
        if array[j]['precio'] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[ultimo] = array[ultimo], array[i + 1]
    return i + 1


# Función de ordenamiento (QuickSort)
def quickSort(array, primero, ultimo):
    if primero < ultimo:
        central = partition(array, primero, ultimo)
        quickSort(array, primero, central - 1)
        quickSort(array, central + 1, ultimo)


# Menú para gestionar la ordenación
def menu_ordenamiento():
    while True:
        print("\n--- Menú de Ordenamiento ---")
        print("1. Agregar álbum")
        print("2. Mostrar álbumes")
        print("3. Ordenar álbumes por precio")
        print("4. Regresar al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_album()
        elif opcion == '2':
            mostrar_albumes()
        elif opcion == '3':
            if not albumes:
                print("\nNo hay álbumes para ordenar.")
            else:
                quickSort(albumes, 0, len(albumes) - 1)
                print("Álbumes ordenados por precio.")
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

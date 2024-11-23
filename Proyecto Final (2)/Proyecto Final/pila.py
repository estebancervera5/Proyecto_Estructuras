# pila.py
carrito = []
LIMITE_PILA = 5


def agregar_al_carrito():
    if len(carrito) >= LIMITE_PILA:
        print("\nEl carrito está lleno. No puedes agregar más álbumes.")
        return

    print("\n--- Agregar un álbum al carrito ---")
    nombre = input("Nombre del álbum: ")
    artista = input("Nombre del artista: ")

    while True:
        try:
            precio = float(input("Precio del álbum: "))  # Validación de precio
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
    carrito.append(album)
    print("Álbum agregado al carrito.")


def mostrar_carrito():
    if not carrito:
        print("\nEl carrito está vacío.")
    else:
        print("\n--- Carrito de Compras ---")
        for i, album in enumerate(reversed(carrito)):
            print(f"{i + 1}. {album['nombre']} - {album['artista']} - ${album['precio']}")


def eliminar_del_carrito():
    if esta_vacia():
        print("\nEl carrito está vacío. No hay álbumes para eliminar.")
    else:
        album = carrito.pop()
        print(f"Álbum '{album['nombre']}' eliminado del carrito.")


def limpiar_pila():
    global carrito
    carrito.clear()
    print("\nLa pila ha sido limpiada.")


def cima_de_pila():
    if esta_vacia():
        print("\nLa pila está vacía.")
    else:
        album = carrito[-1]
        print(f"\nCima de la pila: {album['nombre']} - {album['artista']} - ${album['precio']}")


def tamano_de_pila():
    print(f"\nTamaño actual de la pila: {len(carrito)} de un máximo de {LIMITE_PILA}")


def esta_vacia():
    return len(carrito) == 0


def esta_llena():
    return len(carrito) == LIMITE_PILA


def menu_pilas():
    while True:
        print("\n--- Menú del Carrito (Pilas) ---")
        print("1. Agregar álbum al carrito")
        print("2. Mostrar carrito")
        print("3. Eliminar último álbum del carrito")
        print("4. Limpiar pila")
        print("5. Mostrar cima de pila")
        print("6. Ver si la pila está vacía")
        print("7. Ver si la pila está llena")
        print("8. Ver tamaño de pila")
        print("9. Regresar al Menú Principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_al_carrito()
        elif opcion == '2':
            mostrar_carrito()
        elif opcion == '3':
            eliminar_del_carrito()
        elif opcion == '4':
            limpiar_pila()
        elif opcion == '5':
            cima_de_pila()
        elif opcion == '6':
            if esta_vacia():
                print("\nLa pila está vacía.")
            else:
                print("\nLa pila no está vacía.")
        elif opcion == '7':
            if esta_llena():
                print("\nLa pila está llena.")
            else:
                print("\nLa pila no está llena.")
        elif opcion == '8':
            tamano_de_pila()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")

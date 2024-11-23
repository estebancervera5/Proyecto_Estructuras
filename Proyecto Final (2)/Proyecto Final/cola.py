# cola.py
from collections import deque

cola = deque()
LIMITE_COLA = 5


def agregar_a_cola():
    if len(cola) >= LIMITE_COLA:
        print("\nLa cola está llena. No puedes agregar más álbumes.")
        return

    print("\n--- Agregar un álbum a la cola ---")
    nombre = input("Nombre del álbum: ")
    artista = input("Nombre del artista: ")

    while True:
        try:
            precio = float(input("Precio del álbum: "))
            if precio < 0:
                print("El precio no puede ser negativo. Por favor, ingresa un valor válido.")
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el precio.")

    album = {
        "nombre": nombre,
        "artista": artista,
        "precio": precio
    }
    cola.append(album)
    print("Álbum agregado a la cola.")


def mostrar_cola():
    if esta_vacia():
        print("\nLa cola está vacía.")
    else:
        print("\n--- Cola de álbumes ---")
        for i, album in enumerate(cola):
            print(f"{i + 1}. {album['nombre']} - {album['artista']} - ${album['precio']}")


def eliminar_de_cola():
    if esta_vacia():
        print("\nLa cola está vacía. No hay álbumes para eliminar.")
    else:
        album = cola.popleft()
        print(f"Álbum '{album['nombre']}' eliminado de la cola.")


def limpiar_cola():
    cola.clear()
    print("\nLa cola ha sido limpiada.")


def frente_de_cola():
    if esta_vacia():
        print("\nLa cola está vacía.")
    else:
        album = cola[0]
        print(f"\nFrente de la cola: {album['nombre']} - {album['artista']} - ${album['precio']}")


def tamano_de_cola():
    print(f"\nTamaño actual de la cola: {len(cola)} de un máximo de {LIMITE_COLA}")


def esta_vacia():
    return len(cola) == 0


def esta_llena():
    return len(cola) == LIMITE_COLA


def menu_colas():
    while True:
        print("\n--- Menú de la Cola ---")
        print("1. Agregar álbum a la cola")
        print("2. Mostrar cola")
        print("3. Eliminar álbum del frente")
        print("4. Limpiar cola")
        print("5. Mostrar frente de la cola")
        print("6. Ver si la cola está vacía")
        print("7. Ver si la cola está llena")
        print("8. Ver tamaño de la cola")
        print("9. Regresar al Menú Principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_a_cola()
        elif opcion == '2':
            mostrar_cola()
        elif opcion == '3':
            eliminar_de_cola()
        elif opcion == '4':
            limpiar_cola()
        elif opcion == '5':
            frente_de_cola()
        elif opcion == '6':
            if esta_vacia():
                print("\nLa cola está vacía.")
            else:
                print("\nLa cola no está vacía.")
        elif opcion == '7':
            if esta_llena():
                print("\nLa cola está llena.")
            else:
                print("\nLa cola no está llena.")
        elif opcion == '8':
            tamano_de_cola()
        elif opcion == '9':
            break
        else:
            print("Opción no válida.")

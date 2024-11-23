from arreglo import menu_arreglos
from pila import menu_pilas
from cola import menu_colas
from ordenamiento import menu_ordenamiento
from binaria import menu_busqueda
from Lista import menu_listas
from arbol import menu_arbol  # Importa el menú del árbol
from grafo import menu_kruskal  # Importa el menú para Kruskal

def menu_principal():
    while True:
        print("\n--- Menú Principal de la Tienda de Música ---")
        print("1. Gestión de álbumes (Arreglos)")
        print("2. Carrito de compras (Pilas)")
        print("3. Gestión de pedidos (Colas)")
        print("4. Ordenamiento de álbumes por precio (Quicksort)")
        print("5. Búsqueda de álbum por precio (Búsqueda binaria)")
        print("6. Consultar lista de álbumes (Lista Doble Enlazada)")
        print("7. Gestión de álbumes (Árbol Binario)")  # Nueva opción
        print("8. Gestión de rutas de entrega (Kruskal)")  # Nueva opción de Kruskal
        print("9. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            menu_arreglos()
        elif opcion == '2':
            menu_pilas()
        elif opcion == '3':
            menu_colas()
        elif opcion == '4':
            menu_ordenamiento()
        elif opcion == '5':
            menu_busqueda()
        elif opcion == '6':
            menu_listas()
        elif opcion == '7':
            menu_arbol()
        elif opcion == '8':
            menu_kruskal()
        elif opcion == '9':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()

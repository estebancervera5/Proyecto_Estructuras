class Nodo:
    def __init__(self, nombre, artista, precio):
        self.album = {"nombre": nombre, "artista": artista, "precio": precio}
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    #Método para agregar un álbum al árbol, basado en el precio
    def agregar(self, nombre, artista, precio):
        nuevo = Nodo(nombre, artista, precio)
        if not self.raiz:
            self.raiz = nuevo
            print(f"Álbum '{nombre}' con precio {precio} agregado como raíz.")
        else:
            self._agregar_recursivo(self.raiz, nuevo)

    #Método recursivo para agregar un álbum al árbol, basado en el precio
    def _agregar_recursivo(self, actual, nuevo):
        if nuevo.album["precio"] < actual.album["precio"]:
            if actual.izquierda is None:
                actual.izquierda = nuevo
                print(f"Álbum '{nuevo.album['nombre']}' con precio {nuevo.album['precio']} agregado a la izquierda de '{actual.album['nombre']}'.")
            else:
                self._agregar_recursivo(actual.izquierda, nuevo)
        elif nuevo.album["precio"] > actual.album["precio"]:
            if actual.derecha is None:
                actual.derecha = nuevo
                print(f"Álbum '{nuevo.album['nombre']}' con precio {nuevo.album['precio']} agregado a la derecha de '{actual.album['nombre']}'.")
            else:
                self._agregar_recursivo(actual.derecha, nuevo)
        else:
            print(f"El álbum '{nuevo.album['nombre']}' con precio {nuevo.album['precio']} ya existe en el árbol.")

    # Recorrido Preorden
    def recorrido_preorden(self, nodo):
        if nodo:
            print(f"{nodo.album['nombre']} - {nodo.album['precio']}")
            self.recorrido_preorden(nodo.izquierda)
            self.recorrido_preorden(nodo.derecha)

    # Recorrido Inorden
    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izquierda)
            print(f"{nodo.album['nombre']} - {nodo.album['precio']}")
            self.recorrido_inorden(nodo.derecha)

    # Recorrido Postorden
    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izquierda)
            self.recorrido_postorden(nodo.derecha)
            print(f"{nodo.album['nombre']} - {nodo.album['precio']}")

    # Buscar un álbum en el árbol por precio
    def buscar(self, precio):
        return self._buscar_recursivo(self.raiz, precio)

    def _buscar_recursivo(self, nodo, precio):
        if nodo is None:
            return None
        if precio == nodo.album["precio"]:
            return nodo
        elif precio < nodo.album["precio"]:
            return self._buscar_recursivo(nodo.izquierda, precio)
        else:
            return self._buscar_recursivo(nodo.derecha, precio)

    # Eliminar un álbum por precio
    def eliminar(self, precio):
        self.raiz = self._eliminar_recursivo(self.raiz, precio)

    def _eliminar_recursivo(self, nodo, precio):
        if nodo is None:
            return nodo

        # Si el precio es menor, se va a la izquierda
        if precio < nodo.album["precio"]:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, precio)
        # Si el precio es mayor, se va a la derecha
        elif precio > nodo.album["precio"]:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, precio)
        # Si el precio es igual al precio del nodo actual, se elimina el nodo
        else:
            # Caso 1: Nodo sin hijos
            if nodo.izquierda is None and nodo.derecha is None:
                return None
            # Caso 2: Nodo con un solo hijo
            elif nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            # Caso 3: Nodo con dos hijos
            else:
                # Encontrar el nodo más pequeño en el subárbol derecho
                nodo_minimo = self._encontrar_minimo(nodo.derecha)
                nodo.album = nodo_minimo.album  # Reemplazar el nodo con el mínimo
                nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo_minimo.album["precio"])

        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

# Función del menú para el árbol
def obtener_precio():
    while True:
        try:
            precio = float(input("Introduce el precio del álbum: "))
            return precio
        except ValueError:
            print("¡Error! Por favor, introduce un número válido para el precio.")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            return opcion
        except ValueError:
            print("¡Error! Por favor, introduce un número entero válido para la opción.")

def menu_arbol():
    arbol = ArbolBinario()

    while True:
        print("\n--- Menú de Gestión de Álbumes (Árbol Binario) ---")
        print("1. Agregar álbum al árbol")
        print("2. Recorrido Preorden")
        print("3. Recorrido Inorden")
        print("4. Recorrido Postorden")
        print("5. Buscar álbum por precio")
        print("6. Eliminar álbum por precio")
        print("7. Salir")

        opcion = obtener_opcion()

        if opcion == 1:
            nombre = input("Introduce el nombre del álbum: ")
            artista = input("Introduce el nombre del artista: ")
            precio = obtener_precio()
            arbol.agregar(nombre, artista, precio)
        elif opcion == 2:
            print("\nRecorrido Preorden:")
            arbol.recorrido_preorden(arbol.raiz)
        elif opcion == 3:
            print("\nRecorrido Inorden:")
            arbol.recorrido_inorden(arbol.raiz)
        elif opcion == 4:
            print("\nRecorrido Postorden:")
            arbol.recorrido_postorden(arbol.raiz)
        elif opcion == 5:
            precio = obtener_precio()
            album = arbol.buscar(precio)
            if album:
                print(f"Álbum encontrado: {album.album['nombre']} - {album.album['precio']}")
            else:
                print("Álbum no encontrado.")
        elif opcion == 6:
            precio = obtener_precio()
            arbol.eliminar(precio)
            print(f"Álbum con precio {precio} eliminado (si existía).")
        elif opcion == 7:
            print("Saliendo del menú de árbol binario...")
            break
        else:
            print("Opción no válida.")


class Double_Linked_List:
    class _Nodo:
        def __init__(self, album):
            self.album = album  # Almacenar el objeto álbum
            self.nodo_anterior = None
            self.nodo_siguiente = None

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def __str__(self):
        # Muestra los detalles de los álbumes
        array = []
        nodo_actual = self.cabeza
        while nodo_actual != None:
            array.append(str(nodo_actual.album))
            nodo_actual = nodo_actual.nodo_siguiente
        return str(array) + " Tamaño: " + str(self.tamaño)

    def Agregar(self, album):
        # Agrega un álbum al principio de la lista
        nuevo_nodo = self._Nodo(album)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cabeza.nodo_anterior = nuevo_nodo
            nuevo_nodo.nodo_siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamaño += 1

    def AgregarFinal(self, album):
        # Agrega un álbum al final de la lista
        nuevo_nodo = self._Nodo(album)
        if self.cabeza == None and self.cola == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = self.cola
            self.cola = nuevo_nodo
        self.tamaño += 1

    def Eliminar(self):
        # Elimina el primer álbum de la lista
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        elif self.cabeza != None:
            nodo_eliminado = self.cabeza
            self.cabeza = nodo_eliminado.nodo_siguiente
            nodo_eliminado.nodo_siguiente = None
            self.tamaño -= 1
            return print(f"Álbum eliminado: {nodo_eliminado.album}")
        else:
            return None

    def EliminarFinal(self):
        # Elimina el último álbum de la lista
        if self.tamaño == 0:
            self.cabeza = None
            self.cola = None
        else:
            nodo_eliminado = self.cola
            self.cola = nodo_eliminado.nodo_anterior
            self.cola.nodo_siguiente = None
            nodo_eliminado.nodo_anterior = None
            self.tamaño -= 1
            return print(f"Álbum eliminado: {nodo_eliminado.album}")

    def getAlbum(self, indice):
        # Obtiene un álbum por índice
        if indice == self.tamaño - 1:
            print(self.cola.album)
            return self.cola
        elif indice == 0:
            print(self.cabeza.album)
            return self.cabeza
        elif not (indice >= self.tamaño or indice < 0):
            indice_balanceado = int(self.tamaño / 2)
            if indice <= indice_balanceado:
                nodo_actual = self.cabeza
                contador = 0
                while contador != indice:
                    nodo_actual = nodo_actual.nodo_siguiente
                    contador += 1
                print(nodo_actual.album)
                return nodo_actual
            else:
                nodo_actual = self.cola
                contador = self.tamaño - 1
                while contador != indice:
                    nodo_actual = nodo_actual.nodo_anterior
                    contador -= 1
                print(nodo_actual.album)
                return nodo_actual
        else:
            return None

    def updateAlbum(self, indice, album):
        # Actualiza el álbum en un índice dado
        nodo_objetivo = self.getAlbum(indice)
        if nodo_objetivo != None:
            nodo_objetivo.album = album
        else:
            return None

    def insertAlbum(self, indice, album):
        # Inserta un álbum en el índice dado
        if indice == self.tamaño - 1:
            return self.AgregarFinal(album)
        elif not (indice >= self.tamaño or indice < 0):
            nuevo_nodo = self._Nodo(album)
            nodos_anteriores = self.getAlbum(indice)
            nodos_siguientes = nodos_anteriores.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nuevo_nodo
            nuevo_nodo.nodo_anterior = nodos_anteriores
            nuevo_nodo.nodo_siguiente = nodos_siguientes
            nodos_siguientes.nodo_anterior = nuevo_nodo
            self.tamaño += 1
        else:
            return None

    def removeAlbum(self, indice):
        # Elimina un álbum en el índice dado
        if indice == 0:
            return self.Eliminar()
        elif indice == self.tamaño - 1:
            return self.EliminarFinal()
        elif not (indice >= self.tamaño or indice < 0):
            nodo_removido = self.getAlbum(indice)
            nodos_anteriores = nodo_removido.nodo_anterior
            nodos_siguientes = nodo_removido.nodo_siguiente
            nodos_anteriores.nodo_siguiente = nodos_siguientes
            nodos_siguientes.nodo_anterior = nodos_anteriores
            nodo_removido.nodo_anterior = None
            nodo_removido.nodo_siguiente = None
            self.tamaño -= 1
            return nodo_removido
        else:
            return None

    def reverse(self):
        # Revierte la lista de álbumes
        nodos_revertidos = None
        nodo_actual = self.cabeza
        self.cola = nodo_actual
        while nodo_actual != None:
            nodos_revertidos = nodo_actual.nodo_anterior
            nodo_actual.nodo_anterior = nodo_actual.nodo_siguiente
            nodo_actual.nodo_siguiente = nodos_revertidos
            nodo_actual = nodo_actual.nodo_anterior
        self.cabeza = nodos_revertidos.nodo_anterior


# Menú de operaciones con la lista doblemente enlazada de álbumes
def menu_listas():
    lista = Double_Linked_List()

    while True:
        print("\n--- Menú de Gestión de Álbumes (Lista Doble Enlazada) ---")
        print("1. Agregar al principio (prepend)")
        print("2. Agregar al final (append)")
        print("3. Eliminar el primero (shift)")
        print("4. Eliminar el último (pop)")
        print("5. Ver un álbum por índice (get)")
        print("6. Actualizar un álbum por índice (update)")
        print("7. Insertar un álbum en un índice (insert)")
        print("8. Eliminar un álbum en un índice (remove)")
        print("9. Ver lista de álbumes (mostrar)")
        print("10. Revertir la lista (reverse)")
        print("11. Regresar al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre del álbum: ")
            artista = input("Introduce el nombre del artista: ")
            while True:
                try:
                    año = int(input("Introduce el año del álbum: "))
                    break  # Salir del bucle si el año es válido
                except ValueError:
                    print("El año debe ser un número. Inténtalo de nuevo.")
            album = {"nombre": nombre, "artista": artista, "año": año}
            lista.Agregar(album)

        elif opcion == "2":
            nombre = input("Introduce el nombre del álbum: ")
            artista = input("Introduce el nombre del artista: ")
            while True:
                try:
                    año = int(input("Introduce el año del álbum: "))
                    break
                except ValueError:
                    print("El año debe ser un número. Inténtalo de nuevo.")
            album = {"nombre": nombre, "artista": artista, "año": año}
            lista.AgregarFinal(album)

        elif opcion == "3":
            lista.Eliminar()

        elif opcion == "4":
            lista.EliminarFinal()

        elif opcion == "5":
            indice = int(input("Introduce el índice del álbum a ver: "))
            lista.getAlbum(indice)

        elif opcion == "6":
            indice = int(input("Introduce el índice del álbum a actualizar: "))
            nombre = input("Introduce el nuevo nombre del álbum: ")
            artista = input("Introduce el nuevo artista: ")
            while True:
                try:
                    año = int(input("Introduce el nuevo año del álbum: "))
                    break
                except ValueError:
                    print("El año debe ser un número. Inténtalo de nuevo.")
            album = {"nombre": nombre, "artista": artista, "año": año}
            lista.updateAlbum(indice, album)

        elif opcion == "7":
            indice = int(input("Introduce el índice donde insertar el nuevo álbum: "))
            nombre = input("Introduce el nombre del álbum: ")
            artista = input("Introduce el nombre del artista: ")
            while True:
                try:
                    año = int(input("Introduce el año del álbum: "))
                    break
                except ValueError:
                    print("El año debe ser un número. Inténtalo de nuevo.")
            album = {"nombre": nombre, "artista": artista, "año": año}
            lista.insertAlbum(indice, album)

        elif opcion == "8":
            indice = int(input("Introduce el índice del álbum a eliminar: "))
            lista.removeAlbum(indice)

        elif opcion == "9":
            print(lista)

        elif opcion == "10":
            lista.reverse()

        elif opcion == "11":
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


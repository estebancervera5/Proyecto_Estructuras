class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_ruta(self, origen, destino, costo):
        """Agrega una ruta entre dos puntos con un costo asociado."""
        self.grafo.append([origen, destino, costo])

    def buscar(self, parent, i):
        """Encuentra el conjunto al que pertenece un vértice."""
        if parent[i] == i:
            return i
        return self.buscar(parent, parent[i])

    def unir(self, parent, rank, x, y):
        """Une dos subconjuntos."""
        raizX = self.buscar(parent, x)
        raizY = self.buscar(parent, y)

        if rank[raizX] < rank[raizY]:
            parent[raizX] = raizY
        elif rank[raizX] > rank[raizY]:
            parent[raizY] = raizX
        else:
            parent[raizY] = raizX
            rank[raizX] += 1

    def kruskal(self):
        """Aplica el algoritmo de Kruskal para encontrar las rutas óptimas."""
        resultado = []  # Lista de rutas seleccionadas
        peso_total = 0  # Variable para el peso total
        i = 0
        e = 0

        # Ordenar las rutas por costo
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        parent = []
        rank = []

        # Inicializar los subconjuntos
        for nodo in range(self.V):
            parent.append(nodo)
            rank.append(0)

        # Procesar las rutas
        while e < self.V - 1:
            origen, destino, costo = self.grafo[i]
            i += 1
            raiz_origen = self.buscar(parent, origen)
            raiz_destino = self.buscar(parent, destino)

            if raiz_origen != raiz_destino:
                e += 1
                resultado.append([origen, destino, costo])
                peso_total += costo  # Sumar el costo al peso total
                self.unir(parent, rank, raiz_origen, raiz_destino)

        print("\nRutas de entrega óptimas:")
        for origen, destino, costo in resultado:
            print(f"De {origen} a {destino} con un costo de {costo}.")

        print(f"\nCosto total de las rutas óptimas: {peso_total}")

def menu_kruskal():
    print("\n--- Gestión de Rutas de Entrega ---")
    while True:
        try:
            # Solicitar el número de puntos de entrega
            vertices = int(input("Introduce el número de puntos de entrega (tiendas): "))
            if vertices <= 0:
                print("El número de puntos debe ser mayor a 0.")
                continue
            break
        except ValueError:
            print("Por favor, introduce un número válido.")

    grafo = Grafo(vertices)

    while True:
        print("\nOpciones:")
        print("1. Agregar una ruta")
        print("2. Calcular rutas óptimas (Kruskal)")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                origen = int(input("Introduce el punto de origen: "))
                destino = int(input("Introduce el punto de destino: "))
                costo = int(input("Introduce el costo de la ruta: "))
                if origen >= vertices or destino >= vertices or origen < 0 or destino < 0:
                    print("Los puntos deben estar dentro del rango de 0 a", vertices - 1)
                else:
                    grafo.agregar_ruta(origen, destino, costo)
                    print(f"Ruta de {origen} a {destino} con costo {costo} agregada.")
            except ValueError:
                print("Por favor, introduce valores válidos.")

        elif opcion == '2':
            grafo.kruskal()

        elif opcion == '3':
            print("Saliendo del gestor de rutas...")
            break

        else:
            print("Opción no válida.")

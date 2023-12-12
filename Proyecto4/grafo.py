import os
from collections import deque

class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = []  # Lista de los nodos del grafo
        self.aristas = []  # Lista de las aristas del grafo
        self.dirigido = dirigido  # Indica si el grafo es dirigido o no

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)  # Agrega un nodo 

    def agregar_arista(self, arista):
        self.aristas.append(arista)  # Agrega una arista 
        
    def generar_graphviz(self, nombre_archivo, ruta_guardado='.'):
        # Genera el archivo en formato DOT para visualizar el grafo con Graphviz
        path = os.path.join(ruta_guardado, nombre_archivo)  # Genera la ruta completa del archivo
        with open(path, 'w') as file:
            if self.dirigido:
                file.write('digraph {\n')  # Crea un grafo dirigido
            else:
                file.write('graph {\n')  # Crea un grafo no dirigido
            # Escribe las aristas en el archivo DOT
            for arista in self.aristas:
                if self.dirigido:
                    file.write(f'    {arista.origen.id} -> {arista.destino.id};\n')  # Arista dirigida
                else:
                    file.write(f'    {arista.origen.id} -- {arista.destino.id};\n')  # Arista no dirigida
            file.write('}')
            
    def KruskalD(self):
        # Algoritmo de Kruskal directo
        self.aristas.sort(key=lambda arista: arista.peso)  # Ordena las aristas por peso
        conjunto_nodos = {nodo.id: {nodo} for nodo in self.nodos}
        arbol_expansion = []

        for arista in self.aristas:
            conjunto_origen = conjunto_nodos[arista.origen.id]
            conjunto_destino = conjunto_nodos[arista.destino.id]

            if conjunto_origen != conjunto_destino:
                arbol_expansion.append(arista)
                conjunto_nodos[arista.origen.id] = conjunto_origen.union(conjunto_destino)
                conjunto_nodos[arista.destino.id] = conjunto_origen

        return arbol_expansion

    def KruskalI(self):
        # Algoritmo de Kruskal inverso
        self.aristas.sort(key=lambda arista: -arista.peso)  # Ordena las aristas por peso en orden descendente
        conjunto_nodos = {nodo.id: {nodo} for nodo in self.nodos}
        arbol_expansion = []

        for arista in self.aristas:
            conjunto_origen = conjunto_nodos[arista.origen.id]
            conjunto_destino = conjunto_nodos[arista.destino.id]

            if conjunto_origen != conjunto_destino:
                arbol_expansion.append(arista)
                conjunto_nodos[arista.origen.id] = conjunto_origen.union(conjunto_destino)
                conjunto_nodos[arista.destino.id] = conjunto_origen

        return arbol_expansion

    def Prim(self):
        # Algoritmo de Prim
        nodos_no_agregados = set(self.nodos)
        arbol_expansion = []

        if not nodos_no_agregados:
            return arbol_expansion

        nodo_actual = nodos_no_agregados.pop()
        nodos_no_agregados.add(nodo_actual)

        while nodos_no_agregados:
            aristas_salientes = [arista for arista in self.aristas if arista.origen in nodos_no_agregados and arista.destino in nodos_no_agregados]

            # Verificar que haya aristas salientes
            if aristas_salientes:
                aristas_salientes.sort(key=lambda arista: arista.peso)  # Ordenar aristas por peso
                arista_menor_peso = aristas_salientes[0]
                arbol_expansion.append(arista_menor_peso)

                nodos_no_agregados.remove(arista_menor_peso.origen)
                nodos_no_agregados.remove(arista_menor_peso.destino)
                nodo_actual = arista_menor_peso.destino  # Actualizar el nodo actual
            else:
                # No hay aristas salientes, el nodo actual está aislado
                # Puedes manejar esta situación según tus necesidades, por ejemplo, imprimir un mensaje o tomar otra acción.
                print(f"El nodo {nodo_actual.id} está aislado y no tiene aristas salientes.")
                break  # Romper el bucle en caso de nodo aislado

        return arbol_expansion
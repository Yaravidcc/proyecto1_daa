# grafo.py

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
    
    def Dijkstra(self, s):
        # Diccionario para almacenar las distancias mínimas desde el nodo fuente
        distancias = {nodo: float('inf') for nodo in self.nodos}
        distancias[s] = 0  # Distancia del nodo fuente a sí mismo es 0

        # Cola de prioridad para explorar nodos en el orden de menor distancia
        cola_prioridad = deque([s])

        while cola_prioridad:
            nodo_actual = cola_prioridad.popleft()

            for arista in self.aristas:
                if arista.origen == nodo_actual:
                    distancia_actual = distancias[nodo_actual] + arista.peso  # Si las aristas tienen pesos
                    if distancia_actual < distancias[arista.destino]:
                        distancias[arista.destino] = distancia_actual
                        cola_prioridad.append(arista.destino)

        # Actualizar los atributos de distancia y nombre de los nodos
        for nodo, distancia in distancias.items():
            nodo.distancia = distancia
            nodo.id = f"{nodo.id} ({distancia:.2f})"

        return distancias
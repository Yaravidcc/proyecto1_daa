import os
from collections import deque

class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = []
        self.aristas = []
        self.dirigido = dirigido

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
    
    def grado(self, nodo):
        return sum(1 for arista in self.aristas if arista.conecta_nodo(nodo))

    def BFS(self, s):
        visitados = set()  # Conjunto de nodos visitados
        resultado = Grafo(self.dirigido)  # Grafo resultado
        cola = deque([s])  # Inicializa la cola con el nodo fuente s
        visitados.add(s.id)  # Marca el nodo fuente como visitado

        while cola:
            actual = cola.popleft()  # Obtiene el nodo de la cabeza de la cola
            resultado.agregar_nodo(actual)  # Agrega el nodo al grafo resultado

            for arista in self.aristas:
                if arista.origen == actual and arista.destino.id not in visitados:
                    visitados.add(arista.destino.id)  # Marca el nodo como visitado
                    cola.append(arista.destino)  # Agrega el nodo a la cola
                    resultado.agregar_arista(arista)  # Agrega la arista al grafo resultado
        
        print(f'Nodos en BFS: {len(resultado.nodos)} (esperados: {len(self.nodos)})')
        return resultado

    def DFS_R(self, s):
        visitados = set()  # Conjunto de nodos visitados
        resultado = Grafo(self.dirigido)  # Grafo resultado
        self._DFS_R_helper(s, visitados, resultado)
        
        print(f'Nodos en DFS_R: {len(resultado.nodos)} (esperados: {len(self.nodos)})')
        return resultado

    def _DFS_R_helper(self, actual, visitados, resultado):
        visitados.add(actual.id)  # Marca el nodo como visitado
        resultado.agregar_nodo(actual)  # Agrega el nodo al grafo resultado

        for arista in self.aristas:
            if arista.origen == actual and arista.destino.id not in visitados:
                resultado.agregar_arista(arista)  # Agrega la arista al grafo resultado
                self._DFS_R_helper(arista.destino, visitados, resultado)  # Llamada recursiva

    def DFS_I(self, s):
        visitados = set()  # Conjunto de nodos visitados
        resultado = Grafo(self.dirigido)  # Grafo resultado
        pila = [s]  # Inicializa la pila con el nodo fuente s

        while pila:
            actual = pila.pop()  # Obtiene el nodo de la cima de la pila

            if actual.id not in visitados:
                visitados.add(actual.id)  # Marca el nodo como visitado
                resultado.agregar_nodo(actual)  # Agrega el nodo al grafo resultado

                for arista in self.aristas:
                    if arista.origen == actual and arista.destino.id not in visitados:
                        pila.append(arista.destino)  # Agrega el nodo a la pila
                        resultado.agregar_arista(arista)  # Agrega la arista al grafo resultado

        print(f'Nodos en DFS_I: {len(resultado.nodos)} (esperados: {len(self.nodos)})')
        return resultado
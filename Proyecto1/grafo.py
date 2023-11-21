# grafo.py
import os
class Grafo:
    def __init__(self, dirigido=False):
        self.nodos = []
        self.aristas = []  # Lista para mantener las aristas
        self.dirigido = dirigido

    def agregar_nodo(self, nodo):
        self.nodos.append(nodo)

    def agregar_arista(self, arista):
        self.aristas.append(arista)
        
    def generar_graphviz(self, nombre_archivo, ruta_guardado='.'):
        path = os.path.join(ruta_guardado, nombre_archivo)
        with open(path, 'w') as file:
            if self.dirigido:
                file.write('digraph {\n')
            else:
                file.write('graph {\n')
            for arista in self.aristas:
                if self.dirigido:
                    file.write(f'    {arista.origen.id} -> {arista.destino.id};\n')
                else:
                    file.write(f'    {arista.origen.id} -- {arista.destino.id};\n')
            file.write('}')

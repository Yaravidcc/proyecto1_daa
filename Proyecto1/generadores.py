import random
from nodo import Nodo
from arista import Arista
from grafo import Grafo
import math
import numpy as np
import math
import os


# Función para crear un grafo de malla m x n
def grafoMalla(m, n, dirigido=False):
    grafo = Grafo(dirigido)  # Crea la clase Grafo

    # Crea nodos con etiquetas f'{i}-{j}'
    for i in range(m):
        for j in range(n):
            nodo = Nodo(f'{i}-{j}')  # Crea un nodo con etiquetas 'i-j'
            grafo.agregar_nodo(nodo)  # Agrega el nodo al grafo

    # Crea aristas entre nodos vecinos en la malla
    for i in range(m):
        for j in range(n):
            if i < m - 1:
                # Conecta el nodo con el nodo de la fila siguiente
                arista_horizontal = Arista(grafo.nodos[i * n + j], grafo.nodos[(i + 1) * n + j], dirigido)
                grafo.agregar_arista(arista_horizontal)  # Agrega arista al grafo
            if j < n - 1:
                # Conecta el nodo con el nodo de la columna siguiente
                arista_vertical = Arista(grafo.nodos[i * n + j], grafo.nodos[i * n + j + 1], dirigido)
                grafo.agregar_arista(arista_vertical)  # Agrega arista al grafo

    return grafo  # Grafo creado

# Función para generar un grafo Erdos-Renyi Gn,m
def grafoErdosRenyi(n, m, dirigido=False, auto=False):
    grafo = Grafo(dirigido)  # Crea la clase Grafo

    # Crea nodos 
    for i in range(n):
        nodo = Nodo(str(i)) 
        grafo.agregar_nodo(nodo)  # Agrega nodo al grafo

    edges = set()  # Almacenar las aristas
    # Crea m aristas aleatorias 
    while len(edges) < m:
        origen = random.randint(0, n - 1)
        destino = random.randint(0, n - 1)
        # Verifica arista que no esté repetida
        if origen != destino and ((origen, destino) not in edges) and ((destino, origen) not in edges or not dirigido):
            edges.add((origen, destino))  # Agrega la arista al conjunto
            arista = Arista(grafo.nodos[origen], grafo.nodos[destino], dirigido)
            grafo.agregar_arista(arista)  # Agrega arista al grafo

    return grafo  # Grafo generado

# Función para generar un grafo Gilbert Gn,p
def grafoGilbert(n, p, dirigido=False, auto=False):
    grafo = Grafo(dirigido)  # Crea la clase Grafo

    # Crea nodos 
    for i in range(n):
        nodo = Nodo(str(i))  # Crea un nodo 
        grafo.agregar_nodo(nodo)  # Agrega nodo al grafo

    # Crea aristas con probabilidad p
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < p:  # Verifica si se debe agregar la arista
                arista = Arista(grafo.nodos[i], grafo.nodos[j], dirigido)
                grafo.agregar_arista(arista)  # Agrega la arista al grafo

    return grafo  # Grafo generado

def distancia_entre_nodos(nodo1, nodo2):
    # Calcular la distancia euclidiana entre dos nodos
    return math.sqrt((nodo1.x - nodo2.x)**2 + (nodo1.y - nodo2.y)**2)

# Función para generar un grafo Geográfico Gn,r
def grafoGeografico(n, r, dirigido=False, auto=False):
    grafo = Grafo(dirigido)  # Crea una instancia de la clase Grafo

    # Asigna posiciones aleatorias a los nodos en un espacio unitario
    for i in range(n):
        nodo = Nodo(str(i))  # Crea un nodo con etiqueta numérica
        nodo.x = random.random()  # Asigna una coordenada x aleatoria
        nodo.y = random.random()  # Asigna una coordenada y aleatoria
        grafo.agregar_nodo(nodo)  # Agrega el nodo al grafo

    # Crea aristas según la distancia entre nodos, si es menor o igual a r
    for i in range(n):
        for j in range(i + 1, n):
            if distancia_entre_nodos(grafo.nodos[i], grafo.nodos[j]) <= r:
                arista = Arista(grafo.nodos[i], grafo.nodos[j], dirigido)
                grafo.agregar_arista(arista)  # Agrega la arista al grafo

    return grafo  # Grafo generado

# Función para generar un grafo Barabasi-Albert Gn,d
def grafoBarabasiAlbert(n, d, dirigido=False, auto=False):
    grafo = Grafo(dirigido)  # Crea la clase Grafo

    # Crea nodos 
    for i in range(n):
        nodo = Nodo(str(i))  # Crea un nodo 
        grafo.agregar_nodo(nodo)  # Agrega el nodo al grafo

    # Conecta los primeros d nodos entre sí
    for i in range(min(d, n)):
        for j in range(i + 1, min(d, n)):
            arista = Arista(grafo.nodos[i], grafo.nodos[j], dirigido)
            grafo.agregar_arista(arista)  # Agrega la arista al grafo

    # Conecta los nodos restantes con probabilidad proporcional al grado
    for i in range(d, n):
        target_nodes = random.sample(grafo.nodos[:i], d)  # Selecciona nodos destino
        for node in target_nodes:
            arista = Arista(grafo.nodos[i], node, dirigido)
            grafo.agregar_arista(arista)  # Agrega la arista al grafo

    return grafo  # Grafo generado

# Función para generar un grafo Dorogovtsev-Mendes
def grafoDorogovtsevMendes(n, dirigido=False):
    grafo = Grafo(dirigido)  # Crea la clase Grafo

    # Crea 3 nodos y 3 aristas formando un triángulo inicial
    for i in range(3):
        nodo = Nodo(str(i))  # Crea un nodo con etiqueta numérica
        grafo.agregar_nodo(nodo)  # Agrega el nodo al grafo

    arista1 = Arista(grafo.nodos[0], grafo.nodos[1], dirigido)  # Crea aristas
    arista2 = Arista(grafo.nodos[1], grafo.nodos[2], dirigido)
    arista3 = Arista(grafo.nodos[2], grafo.nodos[0], dirigido)
    grafo.agregar_arista(arista1)  # Agrega las aristas al grafo
    grafo.agregar_arista(arista2)
    grafo.agregar_arista(arista3)

    # Agrega nodos restantes y conecta con nodos aleatorios existentes
    for i in range(3, n):
        random_edge = random.choice(grafo.aristas)  # Elige una arista aleatoria
        nuevo_nodo = Nodo(str(i))  # Crea un nuevo nodo 
        grafo.agregar_nodo(nuevo_nodo)  # Agrega el nodo al grafo
        arista1 = Arista(nuevo_nodo, random_edge.origen, dirigido)  # Crea aristas
        arista2 = Arista(nuevo_nodo, random_edge.destino, dirigido)
        grafo.agregar_arista(arista1)  # Agrega las aristas al grafo
        grafo.agregar_arista(arista2)

    return grafo  # Grafo generado

def guardar_grafo_en_archivo(grafo, modelo, n):
    nombre_archivo = f'{modelo}_{n}.dot'
    grafo.generar_graphviz(nombre_archivo)

# Modelo Gm,n de malla
modelo_malla_30 = grafoMalla(5, 6)  # 5x6 nodos
modelo_malla_30.generar_graphviz('modelo_malla_30.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_malla_100 = grafoMalla(10, 10)  # 10x10 nodos
modelo_malla_100.generar_graphviz('modelo_malla_100.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_malla_500 = grafoMalla(20, 25)  # 20x25 nodos
modelo_malla_500.generar_graphviz('modelo_malla_500.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')

# Modelo Gn,m de Erdös y Rényi
modelo_erdos_30 = grafoErdosRenyi(30, 80)  # 30 nodos, 80 aristas
modelo_erdos_30.generar_graphviz('modelo_erdos_30.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_erdos_100 = grafoErdosRenyi(100, 400)  # 100 nodos, 400 aristas
modelo_erdos_100.generar_graphviz('modelo_erdos_100.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_erdos_500 = grafoErdosRenyi(500, 2500)  # 500 nodos, 2500 aristas
modelo_erdos_500.generar_graphviz('modelo_erdos_500.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')

# Modelo Gn,p de Gilbert
modelo_gilbert_30 = grafoGilbert(30, 0.2)  # 30 nodos, probabilidad 0.2
modelo_gilbert_30.generar_graphviz('modelo_gilbert_30.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_gilbert_100 = grafoGilbert(100, 0.1)  # 100 nodos, probabilidad 0.1
modelo_gilbert_100.generar_graphviz('modelo_gilbert_100.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_gilbert_500 = grafoGilbert(500, 0.05)  # 500 nodos, probabilidad 0.05
modelo_gilbert_500.generar_graphviz('modelo_gilbert_500.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')

# Modelo Gn,r geográfico simple
modelo_geografico_30 = grafoGeografico(30, 0.2)  # 30 nodos, distancia 0.2
modelo_geografico_30.generar_graphviz('modelo_geografico_30.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_geografico_100 = grafoGeografico(100, 0.1)  # 100 nodos, distancia 0.1
modelo_geografico_100.generar_graphviz('modelo_geografico_100.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_geografico_500 = grafoGeografico(500, 0.05)  # 500 nodos, distancia 0.05
modelo_geografico_500.generar_graphviz('modelo_geografico_500.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')

# Variante del modelo Gn,d Barabási-Albert
modelo_barabasi_30 = grafoBarabasiAlbert(30, 3)  # 30 nodos, grado máximo esperado 3
modelo_barabasi_30.generar_graphviz('modelo_barabasi_30.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_barabasi_100 = grafoBarabasiAlbert(100, 5)  # 100 nodos, grado máximo esperado 5
modelo_barabasi_100.generar_graphviz('modelo_barabasi_100.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_barabasi_500 = grafoBarabasiAlbert(500, 8)  # 500 nodos, grado máximo esperado 8
modelo_barabasi_500.generar_graphviz('modelo_barabasi_500.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')

# Modelo Gn Dorogovtsev-Mendes
modelo_dorogovtsev_30 = grafoDorogovtsevMendes(30)  # 30 nodos
modelo_dorogovtsev_30.generar_graphviz('modelo_dorogovtsev_30.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_dorogovtsev_100 = grafoDorogovtsevMendes(100)  # 100 nodos
modelo_dorogovtsev_100.generar_graphviz('modelo_dorogovtsev_100.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')
modelo_dorogovtsev_500 = grafoDorogovtsevMendes(500)  # 500 nodos
modelo_dorogovtsev_500.generar_graphviz('modelo_dorogovtsev_500.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto1\\archivos')

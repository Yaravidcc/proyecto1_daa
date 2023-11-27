from generadores import grafoMalla
from generadores import grafoErdosRenyi
from generadores import grafoGilbert
from generadores import grafoGeografico
from generadores import grafoBarabasiAlbert
from generadores import grafoDorogovtsevMendes
from grafo import Grafo
import random

""" Generar Grafos """

# Generar grafos para Modelo Gm,n de malla
grafo_30 = grafoMalla(5, 6)  # 30 nodos en una malla 5x6
grafo_100 = grafoMalla(10, 10)  # 100 nodos en una malla 10x10
grafo_500 = grafoMalla(25, 20)  # 500 nodos en una malla 25x20

# Generar grafos para Modelo Gn,m de Erdös y Rényi 
grafo_erdos_renyi_30 = grafoErdosRenyi(30, 50)  # 30 nodos, aproximadamente 50 aristas
grafo_erdos_renyi_100 = grafoErdosRenyi(100, 200)  # 100 nodos, aproximadamente 200 aristas
grafo_erdos_renyi_500 = grafoErdosRenyi(500, 1000)  # 500 nodos, aproximadamente 1000 aristas

# Generar grafos para Modelo Gn,p de Gilbert
grafo_gilbert_30 = grafoGilbert(30, 0.2)  # 30 nodos, probabilidad 0.1
grafo_gilbert_100 = grafoGilbert(100, 0.2)  # 100 nodos, probabilidad 0.05
grafo_gilbert_500 = grafoGilbert(500, 0.2)  # 500 nodos, probabilidad 0.02

# Modelo Gn,r geográfico simple
grafo_geografico_30 = grafoGeografico(30, 0.5)  # 30 nodos, radio 0.2
grafo_geografico_100 = grafoGeografico(100, 0.5)  # 100 nodos, radio 0.1
grafo_geografico_500 = grafoGeografico(500, 0.5)  # 500 nodos, radio 0.05

# Variante del modelo Gn,d Barabási-Albert
grafo_barabasi_albert_30 = grafoBarabasiAlbert(30, 2)  # 30 nodos, grado 2
grafo_barabasi_albert_100 = grafoBarabasiAlbert(100, 3)  # 100 nodos, grado 3
grafo_barabasi_albert_500 = grafoBarabasiAlbert(500, 5)  # 500 nodos, grado 5

# Modelo Gn Dorogovtsev-Mendes
grafo_dorogovtsev_mendes_30 = grafoDorogovtsevMendes(30)  # 30 nodos
grafo_dorogovtsev_mendes_100 = grafoDorogovtsevMendes(100)  # 100 nodos
grafo_dorogovtsev_mendes_500 = grafoDorogovtsevMendes(500)  # 500 nodos

""" Aplicar algoritmos BFS y DFS """

# Modelo Gm,n de malla 
resultado_bfs_30 = grafo_30.BFS(grafo_30.nodos[0])
resultado_dfs_r_30 = grafo_30.DFS_R(grafo_30.nodos[0])
resultado_dfs_i_30 = grafo_30.DFS_I(grafo_30.nodos[0])

resultado_bfs_100 = grafo_100.BFS(grafo_100.nodos[0])
resultado_dfs_r_100 = grafo_100.DFS_R(grafo_100.nodos[0])
resultado_dfs_i_100 = grafo_100.DFS_I(grafo_100.nodos[0])

resultado_bfs_500 = grafo_500.BFS(grafo_500.nodos[0])
resultado_dfs_r_500 = grafo_500.DFS_R(grafo_500.nodos[0])
resultado_dfs_i_500 = grafo_500.DFS_I(grafo_500.nodos[0])

# Modelo Gn,m de Erdös y Rényi  

resultado_bfs_erdos_renyi_30 = grafo_erdos_renyi_30.BFS(grafo_erdos_renyi_30.nodos[0])
resultado_dfs_r_erdos_renyi_30 = grafo_erdos_renyi_30.DFS_R(grafo_erdos_renyi_30.nodos[0])
resultado_dfs_i_erdos_renyi_30 = grafo_erdos_renyi_30.DFS_I(grafo_erdos_renyi_30.nodos[0])

resultado_bfs_erdos_renyi_100 = grafo_erdos_renyi_100.BFS(grafo_erdos_renyi_100.nodos[0])
resultado_dfs_r_erdos_renyi_100 = grafo_erdos_renyi_100.DFS_R(grafo_erdos_renyi_100.nodos[0])
resultado_dfs_i_erdos_renyi_100 = grafo_erdos_renyi_100.DFS_I(grafo_erdos_renyi_100.nodos[0])

resultado_bfs_erdos_renyi_500 = grafo_erdos_renyi_500.BFS(grafo_erdos_renyi_500.nodos[0])
resultado_dfs_r_erdos_renyi_500 = grafo_erdos_renyi_500.DFS_R(grafo_erdos_renyi_500.nodos[0])
resultado_dfs_i_erdos_renyi_500 = grafo_erdos_renyi_500.DFS_I(grafo_erdos_renyi_500.nodos[0])

# Modelo Gn,p de Gilbert

resultado_bfs_gilbert_30 = grafo_gilbert_30.BFS(grafo_gilbert_30.nodos[0])
resultado_dfs_r_gilbert_30 = grafo_gilbert_30.DFS_R(grafo_gilbert_30.nodos[0])
resultado_dfs_i_gilbert_30 = grafo_gilbert_30.DFS_I(grafo_gilbert_30.nodos[0])

resultado_bfs_gilbert_100 = grafo_gilbert_100.BFS(grafo_gilbert_100.nodos[0])
resultado_dfs_r_gilbert_100 = grafo_gilbert_100.DFS_R(grafo_gilbert_100.nodos[0])
resultado_dfs_i_gilbert_100 = grafo_gilbert_100.DFS_I(grafo_gilbert_100.nodos[0])

resultado_bfs_gilbert_500 = grafo_gilbert_500.BFS(grafo_gilbert_500.nodos[0])
resultado_dfs_r_gilbert_500 = grafo_gilbert_500.DFS_R(grafo_gilbert_500.nodos[0])
resultado_dfs_i_gilbert_500 = grafo_gilbert_500.DFS_I(grafo_gilbert_500.nodos[0])

# Modelo Gn,r geográfico simple

resultado_bfs_geografico_30 = grafo_geografico_30.BFS(grafo_geografico_30.nodos[0])
resultado_dfs_r_geografico_30 = grafo_geografico_30.DFS_R(grafo_geografico_30.nodos[0])
resultado_dfs_i_geografico_30 = grafo_geografico_30.DFS_I(grafo_geografico_30.nodos[0])

resultado_bfs_geografico_100 = grafo_geografico_100.BFS(grafo_geografico_100.nodos[0])
resultado_dfs_r_geografico_100 = grafo_geografico_100.DFS_R(grafo_geografico_100.nodos[0])
resultado_dfs_i_geografico_100 = grafo_geografico_100.DFS_I(grafo_geografico_100.nodos[0])

resultado_bfs_geografico_500 = grafo_geografico_500.BFS(grafo_geografico_500.nodos[0])
resultado_dfs_r_geografico_500 = grafo_geografico_500.DFS_R(grafo_geografico_500.nodos[0])
resultado_dfs_i_geografico_500 = grafo_geografico_500.DFS_I(grafo_geografico_500.nodos[0])

# Variante del modelo Gn,d Barabási-Albert

resultado_bfs_barabasi_albert_30 = grafo_barabasi_albert_30.BFS(grafo_barabasi_albert_30.nodos[0])
resultado_dfs_r_barabasi_albert_30 = grafo_barabasi_albert_30.DFS_R(grafo_barabasi_albert_30.nodos[0])
resultado_dfs_i_barabasi_albert_30 = grafo_barabasi_albert_30.DFS_I(grafo_barabasi_albert_30.nodos[0])

resultado_bfs_barabasi_albert_100 = grafo_barabasi_albert_100.BFS(grafo_barabasi_albert_100.nodos[0])
resultado_dfs_r_barabasi_albert_100 = grafo_barabasi_albert_100.DFS_R(grafo_barabasi_albert_100.nodos[0])
resultado_dfs_i_barabasi_albert_100 = grafo_barabasi_albert_100.DFS_I(grafo_barabasi_albert_100.nodos[0])

resultado_bfs_barabasi_albert_500 = grafo_barabasi_albert_500.BFS(grafo_barabasi_albert_500.nodos[0])
resultado_dfs_r_barabasi_albert_500 = grafo_barabasi_albert_500.DFS_R(grafo_barabasi_albert_500.nodos[0])
resultado_dfs_i_barabasi_albert_500 = grafo_barabasi_albert_500.DFS_I(grafo_barabasi_albert_500.nodos[0])

# Modelo Gn Dorogovtsev-Mendes

resultado_bfs_dorogovtsev_mendes_30 = grafo_dorogovtsev_mendes_30.BFS(grafo_dorogovtsev_mendes_30.nodos[0])
resultado_dfs_r_dorogovtsev_mendes_30 = grafo_dorogovtsev_mendes_30.DFS_R(grafo_dorogovtsev_mendes_30.nodos[0])
resultado_dfs_i_dorogovtsev_mendes_30 = grafo_dorogovtsev_mendes_30.DFS_I(grafo_dorogovtsev_mendes_30.nodos[0])

resultado_bfs_dorogovtsev_mendes_100 = grafo_dorogovtsev_mendes_100.BFS(grafo_dorogovtsev_mendes_100.nodos[0])
resultado_dfs_r_dorogovtsev_mendes_100 = grafo_dorogovtsev_mendes_100.DFS_R(grafo_dorogovtsev_mendes_100.nodos[0])
resultado_dfs_i_dorogovtsev_mendes_100 = grafo_dorogovtsev_mendes_100.DFS_I(grafo_dorogovtsev_mendes_100.nodos[0])

resultado_bfs_dorogovtsev_mendes_500 = grafo_dorogovtsev_mendes_500.BFS(grafo_dorogovtsev_mendes_500.nodos[0])
resultado_dfs_r_dorogovtsev_mendes_500 = grafo_dorogovtsev_mendes_500.DFS_R(grafo_dorogovtsev_mendes_500.nodos[0])
resultado_dfs_i_dorogovtsev_mendes_500 = grafo_dorogovtsev_mendes_500.DFS_I(grafo_dorogovtsev_mendes_500.nodos[0])

""" Guardar grafos resultantes """

# Modelo Gm,n de malla

resultado_bfs_30.generar_graphviz('malla_30_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_30.generar_graphviz('malla_30_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_30.generar_graphviz('malla_30_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_100.generar_graphviz('malla_100_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_100.generar_graphviz('malla_100_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_100.generar_graphviz('malla_100_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_500.generar_graphviz('malla_500_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_500.generar_graphviz('malla_500_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_500.generar_graphviz('malla_500_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

# Modelo Gn,m de Erdös y Rényi 

resultado_bfs_erdos_renyi_30.generar_graphviz('erdos_renyi_30_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_erdos_renyi_30.generar_graphviz('erdos_renyi_30_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_erdos_renyi_30.generar_graphviz('erdos_renyi_30_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_erdos_renyi_100.generar_graphviz('erdos_renyi_100_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_erdos_renyi_100.generar_graphviz('erdos_renyi_100_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_erdos_renyi_100.generar_graphviz('erdos_renyi_100_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_erdos_renyi_500.generar_graphviz('erdos_renyi_500_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_erdos_renyi_500.generar_graphviz('erdos_renyi_500_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_erdos_renyi_500.generar_graphviz('erdos_renyi_500_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

# Modelo Gn,p de Gilbert

resultado_bfs_gilbert_30.generar_graphviz('gilbert_30_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_bfs_gilbert_30.generar_graphviz('gilbert_30_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_bfs_gilbert_30.generar_graphviz('gilbert_30_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_gilbert_100.generar_graphviz('gilbert_100_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_gilbert_100.generar_graphviz('gilbert_100_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_gilbert_100.generar_graphviz('gilbert_100_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_gilbert_500.generar_graphviz('gilbert_500_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_gilbert_500.generar_graphviz('gilbert_500_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_gilbert_500.generar_graphviz('gilbert_500_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

# Modelo Gn,r geográfico simple

resultado_bfs_geografico_30.generar_graphviz('geografico_30_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_geografico_30.generar_graphviz('geografico_30_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_geografico_30.generar_graphviz('geografico_30_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_geografico_100.generar_graphviz('geografico_100_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_geografico_100.generar_graphviz('geografico_100_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_geografico_100.generar_graphviz('geografico_100_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

resultado_bfs_geografico_500.generar_graphviz('geografico_500_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_r_geografico_500.generar_graphviz('geografico_500_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
resultado_dfs_i_geografico_500.generar_graphviz('geografico_500_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

# Variante del modelo Gn,d Barabási-Albert

grafo_barabasi_albert_30.generar_graphviz('barabasi_albert_30_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_barabasi_albert_30.generar_graphviz('barabasi_albert_30_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_barabasi_albert_30.generar_graphviz('barabasi_albert_30_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

grafo_barabasi_albert_100.generar_graphviz('barabasi_albert_100_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_barabasi_albert_100.generar_graphviz('barabasi_albert_100_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_barabasi_albert_100.generar_graphviz('barabasi_albert_100_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

grafo_barabasi_albert_500.generar_graphviz('barabasi_albert_500_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_barabasi_albert_500.generar_graphviz('barabasi_albert_500_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_barabasi_albert_500.generar_graphviz('barabasi_albert_500_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

# Modelo Gn Dorogovtsev-Mendes

grafo_dorogovtsev_mendes_30.generar_graphviz('dorogovtsev_mendes_30_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_dorogovtsev_mendes_30.generar_graphviz('dorogovtsev_mendes_30_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_dorogovtsev_mendes_30.generar_graphviz('dorogovtsev_mendes_30_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

grafo_dorogovtsev_mendes_100.generar_graphviz('dorogovtsev_mendes_100_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_dorogovtsev_mendes_100.generar_graphviz('dorogovtsev_mendes_100_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_dorogovtsev_mendes_100.generar_graphviz('dorogovtsev_mendes_100_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')

grafo_dorogovtsev_mendes_500.generar_graphviz('dorogovtsev_mendes_500_resultado_bfs.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_dorogovtsev_mendes_500.generar_graphviz('dorogovtsev_mendes_500_resultado_dfs_r.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
grafo_dorogovtsev_mendes_500.generar_graphviz('dorogovtsev_mendes_500_resultado_dfs_i.dot', 'C:\\Users\\yarav\\OneDrive\\Documentos\\MCC\\MATERIAS\\DAA\\Proyecto2\\archivos')
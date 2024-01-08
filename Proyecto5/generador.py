import pygame
import networkx as nx
import random
import os
import imageio

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600

# Inicialización de Pygame y creación de la ventana
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualización de Grafo")

# Función para generar un grafo aleatorio con n nodos
def generar_grafo(n):
    G = nx.random_geometric_graph(n, 0.2)  # Genera un grafo aleatorio
    return G

# Función para dibujar el grafo en la pantalla
def dibujar_grafo(G):
    pos = nx.spring_layout(G)  # Algoritmo de disposición de los nodos
    screen.fill(WHITE)  # Limpia la pantalla con el color blanco

    # Dibujar aristas
    for edge in G.edges():
        start = pos[edge[0]]
        end = pos[edge[1]]
        pygame.draw.line(screen, BLACK, (int(start[0] * WIDTH), int(start[1] * HEIGHT)),
                         (int(end[0] * WIDTH), int(end[1] * HEIGHT)), 1)

    # Dibujar nodos
    for node in G.nodes():
        x, y = pos[node]
        pygame.draw.circle(screen, RED, (int(x * WIDTH), int(y * HEIGHT)), 8)  # Dibuja un nodo como círculo
        
        # Agregar etiquetas a los nodos
        font = pygame.font.Font(None, 18)
        text_surface = font.render(str(node), True, BLUE)  # Crea la etiqueta con el número del nodo y color azul
        screen.blit(text_surface, (int(x * WIDTH) + 10, int(y * HEIGHT) + 10))  # Coloca la etiqueta cerca del nodo

    pygame.display.update()  # Actualiza la pantalla

# Función para capturar un video del grafo
def capturar_video(nombre_archivo, num_frames, duracion_frame, grafo):
    frames = []
    for _ in range(num_frames):
        imagen = pygame.Surface((WIDTH, HEIGHT))
        imagen.blit(screen, (0, 0))
        frames.append(pygame.surfarray.array3d(imagen))

        dibujar_grafo(grafo)
        pygame.display.update()
        pygame.time.delay(duracion_frame)

    ruta_video = os.path.join('videos', nombre_archivo)  # Ruta para guardar el video
    imageio.mimwrite(ruta_video, frames, fps=10)  # Guarda el video con los frames a 10 FPS

    print("Video guardado en:", ruta_video)

# Generar y dibujar el grafo para 100 nodos
grafo_100 = generar_grafo(100)
dibujar_grafo(grafo_100)

# Mostrar el grafo de 100 nodos en la ventana de Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    visualizar_grafo(grafo_100)

# Capturar el video del grafo de 100 nodos
nombre_archivo_video_100 = "grafo_100.gif"
num_frames_100 = 20
duracion_frame_100 = 100
capturar_video(nombre_archivo_video_100, num_frames_100, duracion_frame_100, grafo_100)

# Generar y dibujar el grafo para 500 nodos
grafo_500 = generar_grafo(500)
dibujar_grafo(grafo_500)

# Mostrar el grafo de 500 nodos en la ventana de Pygame
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    visualizar_grafo(grafo_500)

# Capturar el video del grafo de 500 nodos
nombre_archivo_video_500 = "grafo_500.gif"
num_frames_500 = 20
duracion_frame_500 = 100
capturar_video(nombre_archivo_video_500, num_frames_500, duracion_frame_500, grafo_500)

# Cerrar Pygame
pygame.quit()
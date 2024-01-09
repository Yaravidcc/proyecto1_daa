import pygame
import networkx as nx
import random
import os
import imageio

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
WIDTH, HEIGHT = 800, 600

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualización de Grafo")

# Función para generar un grafo aleatorio con n nodos
def generar_grafo(n):
    G = nx.random_geometric_graph(n, 0.2)
    return G

# Función para dibujar el grafo en la pantalla
def dibujar_grafo(G):
    pos = nx.spring_layout(G)  # Algoritmo de resortes para obtener la disposición de los nodos
    screen.fill(WHITE)

    # Dibujar aristas
    for edge in G.edges():
        start = pos[edge[0]]
        end = pos[edge[1]]
        pygame.draw.line(screen, BLACK, (int(start[0] * WIDTH), int(start[1] * HEIGHT)),
                         (int(end[0] * WIDTH), int(end[1] * HEIGHT)), 1)

    # Dibujar nodos
    for node in G.nodes():
        x, y = pos[node]
        pygame.draw.circle(screen, RED, (int(x * WIDTH), int(y * HEIGHT)), 8)  # Cambiar tamaño de los nodos
        
        # Agregar etiquetas a los nodos
        font = pygame.font.Font(None, 18)
        text_surface = font.render(str(node), True, BLUE)  # Color de la etiqueta
        screen.blit(text_surface, (int(x * WIDTH) + 10, int(y * HEIGHT) + 10))  # Ajustar posición de la etiqueta

    pygame.display.update()

# Función para guardar capturas de la ventana como imágenes PNG
def capturar_imagen(nombre_archivo, grafo):
    imagen = pygame.Surface((WIDTH, HEIGHT))
    imagen.blit(screen, (0, 0))

    dibujar_grafo(grafo)
    pygame.display.update()

    ruta_imagen = os.path.join('capturas', f"{nombre_archivo}.png")
    pygame.image.save(screen, ruta_imagen)
    print("Captura guardada en:", ruta_imagen)

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

    ruta_video = os.path.join('videos', f"{nombre_archivo}.gif")
    imageio.mimwrite(ruta_video, frames, fps=10)
    print("Video guardado en:", ruta_video)

    # Llamar a la función para guardar capturas de imágenes PNG
    nombre_archivo_imagen = nombre_archivo.replace(".gif", "")
    capturar_imagen(nombre_archivo_imagen, grafo)

# Llamadas para generar y capturar los videos e imágenes
grafo_100 = generar_grafo(100)
dibujar_grafo(grafo_100)
nombre_archivo_100 = "grafo_100"
num_frames_100 = 20
duracion_frame_100 = 100
capturar_video(nombre_archivo_100, num_frames_100, duracion_frame_100, grafo_100)

grafo_500 = generar_grafo(500)
dibujar_grafo(grafo_500)
nombre_archivo_500 = "grafo_500"
num_frames_500 = 20
duracion_frame_500 = 100
capturar_video(nombre_archivo_500, num_frames_500, duracion_frame_500, grafo_500)

# Mantener la ventana abierta hasta que se cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Cerrar Pygame
pygame.quit()
import pygame
import networkx as nx
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

# Función para generar un grafo aleatorio con n nodos y disposición force-directed (Barnes-Hut)
def generar_grafo_force_directed(n):
    G = nx.random_geometric_graph(n, 0.2)
    pos = nx.spring_layout(G, iterations=50)
    return G, pos

# Función para dibujar el grafo en la pantalla
def dibujar_grafo(G, pos):
    imagen = pygame.Surface((WIDTH, HEIGHT))
    imagen.fill(WHITE)

    # Dibujar aristas
    for edge in G.edges():
        start = pos[edge[0]]
        end = pos[edge[1]]
        pygame.draw.line(imagen, BLACK, (int(start[0] * WIDTH), int(start[1] * HEIGHT)),
                         (int(end[0] * WIDTH), int(end[1] * HEIGHT)), 1)

    # Dibujar nodos
    for node in G.nodes():
        x, y = pos[node]
        pygame.draw.circle(imagen, RED, (int(x * WIDTH), int(y * HEIGHT)), 8)

    return imagen

# Función para capturar un video del grafo visualizado en Pygame
def capturar_video(nombre_archivo, num_frames, duracion_frame, grafo, pos):
    frames = []
    for i in range(num_frames):
        imagen = dibujar_grafo(grafo, pos)
        frames.append(pygame.surfarray.array3d(imagen.copy()))

        # Guardar la imagen como PNG
        ruta_imagen = os.path.join('capturas_barnes_hut', f"{nombre_archivo}_{i}.png")
        pygame.image.save(imagen, ruta_imagen)
        print("Captura guardada en:", ruta_imagen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        pygame.time.delay(duracion_frame)

    ruta_video = os.path.join('videos_barnes_hut', f"{nombre_archivo}.gif")
    imageio.mimsave(ruta_video, frames, fps=10)
    print("Video guardado en:", ruta_video)

# Llamadas para generar y capturar los videos
grafo_100, pos_100 = generar_grafo_force_directed(100)
nombre_archivo_video_100 = "grafo_100"
num_frames_100 = 20
duracion_frame_100 = 100
capturar_video(nombre_archivo_video_100, num_frames_100, duracion_frame_100, grafo_100, pos_100)

grafo_500, pos_500 = generar_grafo_force_directed(500)
nombre_archivo_video_500 = "grafo_500"
num_frames_500 = 20
duracion_frame_500 = 100
capturar_video(nombre_archivo_video_500, num_frames_500, duracion_frame_500, grafo_500, pos_500)

# Cerrar Pygame
pygame.quit()
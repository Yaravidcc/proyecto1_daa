import pygame
import networkx as nx
import os
import imageio.v2 as imageio

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

# Función para generar un grafo aleatorio con n nodos y disposición force-directed (Fruchterman y Reigold )
def generar_grafo_force_directed(n):
    G = nx.random_geometric_graph(n, 0.2)
    pos = nx.spring_layout(G)
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
        pygame.draw.circle(imagen, RED, (int(x * WIDTH), int(y * HEIGHT)), 8)  # Cambiar tamaño de los nodos
        
        # Agregar etiquetas a los nodos
        font = pygame.font.Font(None, 18)
        text_surface = font.render(str(node), True, BLUE)  # Color de la etiqueta
        imagen.blit(text_surface, (int(x * WIDTH) + 10, int(y * HEIGHT) + 10))  # Ajustar posición de la etiqueta

    return imagen

# Función para capturar un video del grafo visualizado en Pygame
def capturar_video(nombre_archivo, num_frames, duracion_frame, grafo, pos):
    for _ in range(num_frames):
        imagen = dibujar_grafo(grafo, pos)
        
        # Crear una nueva superficie para cada frame
        frame = pygame.Surface((WIDTH, HEIGHT))
        frame.blit(imagen, (0, 0))
        
        # Guardar la imagen como PNG
        ruta_imagen = os.path.join('capturas_fruchterman_reigold', f"{nombre_archivo}_{_}.png")
        pygame.image.save(frame, ruta_imagen)
        print("Captura guardada en:", ruta_imagen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()
        pygame.time.delay(duracion_frame)

    # Lista con las rutas de las imágenes guardadas
    rutas_frames = [
        os.path.join('capturas_fruchterman_reigold', f"{nombre_archivo}_{i}.png") for i in range(num_frames)
    ]

    ruta_video = os.path.join('videos_fruchterman_reigold', f"{nombre_archivo}.gif")
    with imageio.get_writer(ruta_video, mode='I', fps=10) as writer:
        for ruta_frame in rutas_frames:
            imagen_frame = imageio.imread(ruta_frame)
            writer.append_data(imagen_frame)

    print("Video guardado en:", ruta_video)

# Llamadas para generar y capturar los videos
grafo_100, pos_100 = generar_grafo_force_directed(100)
nombre_archivo_video_100 = "grafo_100"
num_frames_100 = 5
duracion_frame_100 = 100
capturar_video(nombre_archivo_video_100, num_frames_100, duracion_frame_100, grafo_100, pos_100)

grafo_500, pos_500 = generar_grafo_force_directed(500)
nombre_archivo_video_500 = "grafo_500"
num_frames_500 = 5
duracion_frame_500 = 100
capturar_video(nombre_archivo_video_500, num_frames_500, duracion_frame_500, grafo_500, pos_500)

# Cerrar Pygame
pygame.quit()
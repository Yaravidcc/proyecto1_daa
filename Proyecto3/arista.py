# arista.py
class Arista:
    def __init__(self, origen, destino, peso=1, dirigido=False):
        self.origen = origen
        self.destino = destino
        self.peso = peso  # Peso o distancia entre nodos
        self.dirigido = dirigido
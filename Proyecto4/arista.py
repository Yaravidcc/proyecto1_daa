# arista.py
class Arista:
    def __init__(self, origen, destino, peso=None, dirigido=False):
        self.origen = origen
        self.destino = destino
        self.peso = peso  # Añadir el atributo peso
        self.dirigido = dirigido
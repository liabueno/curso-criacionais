# Classe Dragao sem o padrao Builder
class Dragao:
    def __init__(self, asas=False, fogo=False):
        # Atributos diretamente definidos no construtor
        self.asas = asas  # Se o dragao tem asas
        self.fogo = fogo  # Se o dragao pode soltar fogo

# Criacao direta de um dragao com asas e fogo
dragao = Dragao(asas=True, fogo=True)

# Exibe o dragao criado
print(dragao.__dict__)  # Saida esperada: {'asas': True, 'fogo': True}
# Classe DragaoBuilder implementando o padrao Builder
class DragaoBuilder:
    def __init__(self):
        # Inicializa o dicionario 'dragao', que vai armazenar as caracteristicas do dragao
        self.dragao = {}

    # Metodo para adicionar asas ao dragao
    def adicionar_asas(self):
        self.dragao["asas"] = True  # Marca que o dragao tem asas
        return self  # Retorna a instancia do Builder para permitir o encadeamento de metodos

    # Metodo para adicionar fogo ao dragao
    def adicionar_fogo(self):
        self.dragao["fogo"] = True  # Marca que o dragao tem a habilidade de soltar fogo
        return self  # Retorna a instancia do Builder para permitir o encadeamento de metodos

    # Metodo que retorna o "produto final" (o dragao configurado)
    def build(self):
        return self.dragao  # Retorna o dicionario 'dragao', que contem as caracteristicas

# Criacao de um dragao com asas e fogo usando o Builder
dragao = DragaoBuilder().adicionar_asas().adicionar_fogo().build()

# Exibe o dragao criado
print(dragao)  # Saida esperada: {'asas': True, 'fogo': True}
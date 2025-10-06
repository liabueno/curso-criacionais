import copy  # Importa o modulo copy para fazer copias profundas (deep copy)

# Classe que representa um Golem
class Golem:
    def __init__(self, poder):
        self.poder = poder  # Atributo que define o tipo de poder do golem (ex: "Fogo", "Gelo")

    # Metodo clone que retorna uma copia profunda do proprio objeto
    def clone(self):
        return copy.deepcopy(self)  # Garante que ate estruturas internas sejam copiadas corretamente

# Criacao do golem original com poder de fogo
golem_original = Golem("Fogo")

# Clonagem do golem original usando o metodo clone (Prototype)
golem_clone = golem_original.clone()
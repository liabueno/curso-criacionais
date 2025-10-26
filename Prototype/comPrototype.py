import copy  # Importa o módulo copy para fazer cópias profundas (deep copy)

# Classe que representa um Golem
class Golem:
    def __init__(self, poder):
        self.poder = poder  # Atributo que define o tipo de poder do golem (ex: "Fogo", "Gelo")

    # Método clone que retorna uma cópia profunda do próprio objeto
    def clone(self):
        return copy.deepcopy(self)  # Garante que até estruturas internas sejam copiadas corretamente

# Criação do golem original com poder de fogo
golem_original = Golem("Fogo")

# Clonagem do golem original usando o método clone (Prototype)
golem_clone = golem_original.clone()

# Saídas
print("Poder do golem original:", golem_original.poder)
print("Poder do golem clone:", golem_clone.poder)

# Verifica se são objetos diferentes na memória
print("São o mesmo objeto na memória?", golem_original is golem_clone)

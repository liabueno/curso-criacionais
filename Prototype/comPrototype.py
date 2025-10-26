# Define uma classe chamada Golem
class Golem:
    # Método construtor da classe
    def __init__(self, poder):
        # Atributo 'poder' é atribuido ao objeto
        self.poder = poder

# Cria o golem original
golem_original = Golem("Fogo")

# Cria um novo golem com o mesmo poder, manualmente
golem_clone = Golem(golem_original.poder)

# Saídas
print("Poder do golem original:", golem_original.poder)
print("Poder do golem clone:", golem_clone.poder)

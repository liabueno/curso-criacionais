# Classe base Arma, representando uma arma generica
class Arma:
    def usar(self):
        pass  # Metodo que sera sobrescrito pelas subclasses

# Classe Espada que herda de Arma
class Espada(Arma):
    def usar(self):
        print("Cortando com espada!")  # Acao especifica da espada

# Uso sem o Factory Method
arma = Espada()  # Criacao direta de uma espada
arma.usar()  # Usa a espada, resultando na acao "Cortando com espada!"
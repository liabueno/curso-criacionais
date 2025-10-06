# Classe base para Armas
class Arma:
    def usar(self): 
        pass

# Classe base para Armaduras
class Armadura:
    def proteger(self): 
        pass

# Implementacao concreta de uma arma com efeito de fogo
class FogoArma(Arma):
    def usar(self):
        print("Ataque de fogo!")

# Implementacao concreta de uma armadura com resistencia ao gelo
class FogoArmadura(Armadura):
    def proteger(self):
        print("Protecao contra gelo!")

# Codigo cliente instancia diretamente os objetos concretos
arma = FogoArma()         # Criacao direta da arma
armadura = FogoArmadura() # Criacao direta da armadura

# Uso dos objetos criados
arma.usar()        # Saida: Ataque de fogo!
armadura.proteger()  # Saida: Protecao contra gelo!
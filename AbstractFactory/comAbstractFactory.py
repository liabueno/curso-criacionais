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

# Fabrica que cria uma familia de objetos relacionados ao fogo
class FabricaFogo:
    def criar_arma(self):
        return FogoArma()  # Retorna uma instancia de arma de fogo

    def criar_armadura(self):
        return FogoArmadura()  # Retorna uma instancia de armadura de fogo

# Codigo cliente usa a fabrica, sem saber exatamente quais classes estao por tras
fabrica = FabricaFogo()
arma = fabrica.criar_arma()
armadura = fabrica.criar_armadura()

# Uso dos objetos criados
arma.usar()        # Saida: Ataque de fogo!
armadura.proteger()  # Saida: Protecao contra gelo!
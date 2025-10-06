# Classe base Arma, representando uma arma generica
class Arma:
    def usar(self):
        pass  # Metodo abstrato que sera implementado por subclasses

# Classe Espada que herda de Arma, representando uma espada
class Espada(Arma):
    def usar(self):
        # Implementacaoo do metodo 'usar' para a espada
        print("Cortando com espada!")  # Acao especifica da espada

# Classe base Ferreiro, responsavel por criar armas
class Ferreiro:
    def criar_arma(self): 
        pass  # Metodo abstrato para criar uma arma, sera implementado pela subclasse

# Classe FerreiroEspada, responsavel por criar espadas
class FerreiroEspada(Ferreiro):
    def criar_arma(self):
        return Espada()  # Retorna uma nova instancia de Espada

# Uso do Factory Method
ferreiro = FerreiroEspada()  # Cria um ferreiro especializado em espadas
arma = ferreiro.criar_arma()  # O ferreiro cria uma espada
arma.usar()  # Usa a espada, resultando na acao "Cortando com espada!"
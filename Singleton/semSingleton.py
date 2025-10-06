# Classe ConfiguracaoTrono sem Singleton
class ConfiguracaoTrono:
    def __init__(self):
        # Cada instancia pode ter seu proprio valor
        self.valor = "Default"

# Criacao da primeira instancia (config1)
config1 = ConfiguracaoTrono()
# Criacao da segunda instancia (config2), que pode ser diferente de config1
config2 = ConfiguracaoTrono()

# Verifica se config1 e config2 sao a mesma instancia
print(config1 is config2)  # Saida: False
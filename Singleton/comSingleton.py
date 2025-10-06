# Classe ConfiguracaoTrono implementando o padrao Singleton
class ConfiguracaoTrono:
    # Atributo de classe que mantem a instancia unica
    _instancia = None

    def __new__(cls):
        # Verifica se a instancia ja foi criada
        if cls._instancia is None:
            # Se nao, cria uma nova instancia
            cls._instancia = super().__new__(cls)
            # Inicializa o valor da configuracao
            cls._instancia.valor = "Default"
        # Retorna a instancia unica
        return cls._instancia

# Criacao da primeira instancia (config1)
config1 = ConfiguracaoTrono()
# Criacao da segunda instancia (config2), que sera a mesma que config1
config2 = ConfiguracaoTrono()

# Verifica se config1 e config2 sao a mesma instancia
print(config1 is config2)  # Saida: True
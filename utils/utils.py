from unidecode import unidecode

def adicionar_remocao_acentos():
    def remover_acentos(self):
        return unidecode(self)
    setattr(str, "sem_acento", remover_acentos)
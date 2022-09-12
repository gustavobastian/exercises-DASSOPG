class Papel:
    texto=""

    def __init__(self, text):
        self.texto=text
    
    def escribir(self,texto2):
        self.texto+=texto2
    def __str__(self):
        return str(self.texto)
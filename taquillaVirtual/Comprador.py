class Comprador:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def get_nombre(self):
        return self.nombre

    def get_documento(self):
        return self.documento

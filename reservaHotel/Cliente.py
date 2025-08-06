class Cliente:
    def __init__(self):
        self.nombre = ""
        self.telefono = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_telefono(self):
        return self.telefono

    def __str__(self):
        return f"Cliente{{nombre='{self.nombre}', telefono='{self.telefono}'}}"

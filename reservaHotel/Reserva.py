class Reserva:
    def __init__(self):
        self.numero_habitacion = 0
        self.cantidad_noches = 0
        self.cliente = None

    def set_numero_habitacion(self, numero):
        self.numero_habitacion = numero

    def get_numero_habitacion(self):
        return self.numero_habitacion

    def set_cantidad_noches(self, noches):
        self.cantidad_noches = noches

    def get_cantidad_noches(self):
        return self.cantidad_noches

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_cliente(self):
        return self.cliente

    def __str__(self):
        return (f"\nResumen Reserva:\n"
                f" - Número de habitación: {self.numero_habitacion}\n"
                f" - Cantidad de noches: {self.cantidad_noches}\n"
                f" - Cliente: {self.cliente}")

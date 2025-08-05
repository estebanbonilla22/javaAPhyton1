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


def main():
    cliente = Cliente()
    cliente.set_nombre(input("Ingrese el nombre del cliente: "))
    cliente.set_telefono(input("Ingrese el teléfono del cliente: "))

    reserva = Reserva()

    try:
        numero_habitacion = int(input("Ingrese el número de habitación: "))
        cantidad_noches = int(input("Ingrese la cantidad de noches: "))
    except ValueError:
        print("Error: Debe ingresar números válidos.")
        return

    reserva.set_numero_habitacion(numero_habitacion)
    reserva.set_cantidad_noches(cantidad_noches)
    reserva.set_cliente(cliente)

    print(reserva)


if __name__ == "__main__":
    main()

from cliente import Cliente
from reserva import Reserva

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

class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - Fecha: {self.fecha}"


class Comprador:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def __str__(self):
        return f"Comprador: {self.nombre}, Documento: {self.documento}"


def main():
    partido = Partido("Deportes Quindío", "América de Cali", "15/08/2025")

    disponibles_norte = 100
    disponibles_sur = 100
    disponibles_vip = 20

    precio_norte = 50000
    precio_sur = 50000
    precio_vip = 200000

    dinero_recaudado = 0
    continuar = False

    while not continuar:
        print("\n===== Taquilla Virtual - Partido =====")
        print(f"Partido: {partido}")
        print("""
1. Comprar Boleta
2. Consultar Disponibilidad
3. Ver Dinero Recaudado
4. Salir del Sistema
""")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            documento = input("Ingrese su documento: ")
            comprador = Comprador(nombre, documento)

            print("""
Seleccione la localidad:
1. Norte
2. Sur
3. VIP
""")
            try:
                tipo_localidad = int(input("Ingrese opción: "))
            except ValueError:
                print("Opción inválida.")
                continue

            try:
                cantidad = int(input("¿Cuántas boletas desea comprar? "))
            except ValueError:
                print("Cantidad inválida.")
                continue

            disponibles = 0
            precio_unitario = 0
            localida

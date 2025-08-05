class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha

    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante} - {self.fecha}"


class Comprador:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def get_nombre(self):
        return self.nombre

    def get_documento(self):
        return self.documento


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
        print(f"""
        Taquilla Virtual - Partido
        Partido: {partido}

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
            seleccion = input("Ingrese el número de la localidad: ")

            try:
                tipo_localidad = int(seleccion)
            except ValueError:
                print("Opción inválida.")
                continue

            cantidad_str = input("¿Cuántas boletas desea comprar? ")

            try:
                cantidad = int(cantidad_str)
            except ValueError:
                print("Cantidad inválida.")
                continue

            disponibles = 0
            precio_unitario = 0
            localidad = ""

            if tipo_localidad == 1:
                disponibles = disponibles_norte
                precio_unitario = precio_norte
                localidad = "Norte"
            elif tipo_localidad == 2:
                disponibles = disponibles_sur
                precio_unitario = precio_sur
                localidad = "Sur"
            elif tipo_localidad == 3:
                disponibles = disponibles_vip
                precio_unitario = precio_vip
                localidad = "VIP"
            else:
                print("Opción de localidad inválida.")
                continue

            if cantidad <= disponibles:
                total = cantidad * precio_unitario
                dinero_recaudado += total

                if tipo_localidad == 1:
                    disponibles_norte -= cantidad
                elif tipo_localidad == 2:
                    disponibles_sur -= cantidad
                elif tipo_localidad == 3:
                    disponibles_vip -= cantidad

                print("\n¡Compra exitosa!")
                print(f"Comprador: {comprador.get_nombre()}")
                print(f"Documento: {comprador.get_documento()}")
                print(f"Localidad: {localidad}")
                print(f"Cantidad: {cantidad}")
                print(f"Total Pagado: ${total}\n")
            else:
                print(f"No hay suficientes boletas disponibles. Boletas disponibles: {disponibles}")

        elif opcion == "2":
            total_disponibles = disponibles_norte + disponibles_sur + disponibles_vip
            print("\nDisponibilidad actual:")
            print(f"Norte: {disponibles_norte}")
            print(f"Sur: {disponibles_sur}")
            print(f"VIP: {disponibles_vip}")
            print(f"TOTAL: {total_disponibles}\n")

        elif opcion == "3":
            print(f"\nDinero recaudado:\nTotal en ventas: ${dinero_recaudado}\n")

        elif opcion == "4":
            print("Gracias por usar la Taquilla Virtual.")
            continuar = True

        else:
            print("Opción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()

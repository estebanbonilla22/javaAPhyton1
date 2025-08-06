from mascota_u import MascotaU

def main():
    monitores = {
        "101": MascotaU("Ana Pérez", "101", "Feria Universidad", 0),
        "102": MascotaU("Carlos Rojas", "102", "Visita Colegio", 0),
        "103": MascotaU("Arle Morales", "103", "Evento de Jóvenes Down", 0),
        "104": MascotaU("Santiago Leyton", "104", "Adopción de Perros", 0),
        "105": MascotaU("Marlon Charro", "105", "Inducción", 0),
    }

    continuar = True

    while continuar:
        print("\nIngrese la opción:")
        print("1. Registrar horas de un monitor")
        print("2. Ver estado de todos los monitores")
        print("3. Salir del sistema")
        opcion = input("Opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del monitor: ")
            if codigo in monitores:
                try:
                    horas = float(input("Ingrese el número de horas a registrar: "))
                except ValueError:
                    print("Debe ingresar un número válido.")
                    continue

                monitor = monitores[codigo]
                monitor.registrar_horas(horas)
                print(f"Tiene {monitor.get_horas_acumuladas()} horas.\n{monitor.verificar_estado()}")
            else:
                print("Código no encontrado.")

        elif opcion == "2":
            print("\nEstado de todos los monitores:")
            for monitor in monitores.values():
                print(monitor)

        elif opcion == "3":
            continuar = False
            print("Saliendo del sistema...")

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()

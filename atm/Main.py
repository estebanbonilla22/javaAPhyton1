from atm import Atm

def main():
    cuenta_bancaria = Atm("Juan Perez", "123-321", 20000)
    cuenta_destino = Atm("Ana Gomez", "321-123", 30000)

    opciones = [
        "Consultar saldo",
        "Retirar dinero",
        "Depositar dinero",
        "Transferir a otra cuenta",
        "Salir"
    ]

    continuar = True

    while continuar:
        print("\n--- Menú ATM ---")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion}")
        try:
            seleccion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

        if seleccion == 1:
            print(f"Saldo actual: ${cuenta_bancaria.get_saldo()}")
        elif seleccion == 2:
            try:
                monto_r = float(input("Ingrese el monto a retirar: "))
                if cuenta_bancaria.retirar(monto_r):
                    print(f"Retiro exitoso. Nuevo saldo: ${cuenta_bancaria.get_saldo()}")
                else:
                    print("Fondos insuficientes.")
            except ValueError:
                print("Monto inválido.")
        elif seleccion == 3:
            try:
                monto_d = float(input("Ingrese el monto a depositar: "))
                cuenta_bancaria.depositar(monto_d)
                print(f"Depósito exitoso. Nuevo saldo: ${cuenta_bancaria.get_saldo()}")
            except ValueError:
                print("Monto inválido.")
        elif seleccion == 4:
            try:
                monto_t = float(input("Ingrese el monto a transferir: "))
                if cuenta_bancaria.transferir(cuenta_destino, monto_t):
                    print("Transferencia exitosa.")
                else:
                    print("Fondos insuficientes para transferir.")
            except ValueError:
                print("Monto inválido.")
        elif seleccion == 5:
            continuar = False
        else:
            print("Opción no válida.")

    print("Gracias por usar el ATM.")


if __name__ == "__main__":
    main()

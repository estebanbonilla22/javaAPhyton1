class Atm:
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_numero_cuenta(self):
        return self.numero_cuenta

    def set_numero_cuenta(self, numero):
        self.numero_cuenta = numero

    def get_saldo(self):
        return self.saldo

    def depositar(self, monto):
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        if monto > 0 and self.saldo >= monto:
            self.saldo -= monto
            return True
        else:
            return False

    def transferir(self, cuenta_destino, monto):
        if self.saldo >= monto:
            self.retirar(monto)
            cuenta_destino.depositar(monto)
            return True
        else:
            return False

    def __str__(self):
        return f"Atm{{titular='{self.titular}', numeroCuenta='{self.numero_cuenta}', saldo={self.saldo}}}"


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

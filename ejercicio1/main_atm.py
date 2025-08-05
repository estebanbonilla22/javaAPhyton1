from ejercicio1.atm import retirar_dinero

def main():
    print("=== Ejecutando ejercicio: atm ===")
    saldo = 1000
    monto = 200
    nuevo_saldo, mensaje = retirar_dinero(saldo, monto)
    print(mensaje)

if __name__ == "__main__":
    main()

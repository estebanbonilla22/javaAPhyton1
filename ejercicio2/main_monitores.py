from ejercicio2.monitores import calcular_precio_final

def main():
    print("=== Ejecutando ejercicio: monitores ===")
    total = calcular_precio_final(150.0, 3, 0.1)
    print(f"Precio final con descuento: ${total}")

if __name__ == "__main__":
    main()

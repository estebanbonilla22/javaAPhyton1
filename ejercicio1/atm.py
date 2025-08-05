def retirar_dinero(saldo, monto):
    if monto <= 0:
        return saldo, "El monto debe ser mayor que cero"
    if monto > saldo:
        return saldo, "Fondos insuficientes"
    saldo -= monto
    return saldo, f"Retiro exitoso. Nuevo saldo: {saldo}"

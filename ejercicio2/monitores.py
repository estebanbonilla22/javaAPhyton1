def calcular_precio_final(precio_unitario, cantidad, descuento):
    subtotal = precio_unitario * cantidad
    total = subtotal * (1 - descuento)
    return round(total, 2)

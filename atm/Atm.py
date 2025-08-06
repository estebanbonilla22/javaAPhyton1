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

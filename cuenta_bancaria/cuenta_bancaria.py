class CuentaBancaria:

    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance

    def generar_balance(self):
        print(self.balance)

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

    def retirar (self, monto):
        if monto < 0:
            self.balance -= monto

    def transferir(self, monto):
        if monto > 0 and self.balance >= monto:
            self.retirar(monto)
            print(f"Se ha transferido {monto}.")
        else:
            print("Transferencia no válida. Verifique el monto y el saldo disponible.")

mi_cuenta = CuentaBancaria("100-222-333", "Lady Vader", 666)

mi_cuenta.generar_balance()
mi_cuenta.transferir(66)



    

        
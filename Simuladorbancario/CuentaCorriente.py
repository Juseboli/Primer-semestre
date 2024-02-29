class CuentaCorriente:
    #aqui va el codigo de cuenta coriiente
    """-----------------------------------
    #Atributos
    -----------------------------------"""
    Saldo=0
    
    """-----------------------------------
    #Metodos
    -----------------------------------"""

    def Consignar(self, monto):
        self.Saldo += monto
    
    def ConsultarSaldocorriente(self):
        return "Su Saldo es" + self.Saldo()
    
    def retirartodo(self):
        return self.Saldo-self.Saldo
    
    def retirar(self,monto):
        self.Saldo -= monto
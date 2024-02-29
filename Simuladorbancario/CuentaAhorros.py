class CuentaAhorros:
    #aqui va el codigo de la cuneta de ahorros
    """---------------------------------------
    #Atributos
    ---------------------------------------"""
    saldo=0
    interesmensual=0
    
    """---------------------------------------
    #Metodos
    ---------------------------------------"""

    def ConsultarSaldoAhorros(self):
        return "su saldo es" + self.saldo
    
    def retirar(self,monto):
        return self-monto

    def retirartodo(self):
        return self.saldo-self.saldo
    
    def consignar(self,monto):
        return self.saldo+monto
    
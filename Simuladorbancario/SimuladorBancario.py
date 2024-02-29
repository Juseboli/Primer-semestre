from CuentaCorriente import CuentaCorriente
from CuentaAhorros import CuentaAhorros
from CDT import CDT

class SimiladorBancario:
    #aqui va el codigo de simulador bancario
    """-------------------------------------
    #Atributos
    -------------------------------------"""
    cedula=0
    nombre=""
    mesactual=0
    
    """-------------------------------------
    #Asociaciones
    -------------------------------------"""

    corriente = CuentaCorriente()
    ahorros = CuentaAhorros()
    cdt = CDT()

    """-------------------------------------
    #Metodos
    -------------------------------------"""

    def comsignarcuentacorriente(self,monto):
        self.corriente.Consignar(monto)

    def ConsultarSaldoTotal(self):
        return "su saldo total es" +(self.ahorros.saldo+self.corriente.Saldo)
    
    def consignardeahorrosacorriente(self):
        self.corriente.Consignar(self.ahorros.ConsultarSaldoAhorros)
        self.ahorros.retirar(self.ahorros.ConsultarSaldoAhorros)

    def consultarsaldocorriente(self):
        return self.corriente.ConsultarSaldocorriente
    
    def retirartotal(self):
        return (self.ahorros.retirartodo+self.corriente.retirartodo)
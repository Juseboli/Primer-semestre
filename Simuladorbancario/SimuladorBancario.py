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
    # 1=normal, 2=platino y 3=VIP
    -------------------------------------"""

    tipocliente=0
    
    """-------------------------------------
    #Asociaciones
    -------------------------------------"""

    corriente = CuentaCorriente()
    ahorros = CuentaAhorros()
    cdt = CDT()

    """-------------------------------------
    #Metodos
    -------------------------------------"""

    def retirarmonto(self, monto):
        descuento = monto * 0.01
        self.saldo -= monto
        self.saldo -= descuento

    def cambiartipocliente(self, ntipocliente):
        self.tipocliente = ntipocliente

    def __init__(cedula, nombre, mesactual, tipocliente):
        self.cedula = cedula
        self.nombre = nombre
        self.mesactual = mesactual
        self.tipocliente = tipocliente

    def comsignarcuentacorriente(self,monto):
        self.corriente.Consignar(monto)

    def ConsultarSaldoTotal(self):
        return "su saldo total es" +(self.ahorros.saldo+self.corriente.Saldo)
    
    def consignardeahorrosacorriente(self):
        self.corriente.Consignar(self.ahorros.ConsultarSaldoAhorros)
        self.ahorros.retirar(self.ahorros.ConsultarSaldoAhorros)

    def consultarsaldocorriente(self):
        return "su saldo es " + self.corriente.ConsultarSaldocorriente
    
    def Duplicarahorro(self):
        self.ahorros.ConsultarSaldoAhorros(self.ahorros.ConsultarSaldoAhorros())
    
    # forma 1
    def retirartodo(self):
        total = self.ConsultarSaldoTotal()
        self.ahorros.retirar(self.ahorros.ConsultarSaldoAhorros)
        self.corriente.retirar(self.corriente.ConsultarSaldocorriente)
        return "retiraste total:"+total

    #forma 2
    # def retirartotal(self):
    #     self.consignardeahorrosacorriente
    #     self.corriente.retirar(self.corriente.ConsultarSaldocorriente)

    #     return ""
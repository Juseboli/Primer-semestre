from Fecha import Fecha

class Empleado:
    # Aqui va el codigo del empleado

    """----------------------------
    Atributos 
    ----------------------------"""
    nombre = ""
    apellido = ""
    """----------------------------
    # 1 = Masculino y 2 = Femenino
    ----------------------------"""
    
    sexo = 0
    salario = 0
    numeroHijOs = 0

    """----------------------------
    # Asociaciones
    ----------------------------"""
    
    fechanacimiento = Fecha()
    fechaingreso = Fecha()

    """----------------------------
    # Metodos
    ----------------------------"""

    def calculardiferenciasalarial(self,otroempleado):
        diferenciasalarial = self.salario - otroempleado
        return """La Diferencia Ssalarial es""" + diferenciasalarial

    def calcularauxilioeducativo(self,porcentaje):
        auxilioeducativo = (porcentaje*self.salario) * self.numeroHijos
        return """Su Auxilio educativo es""" + auxilioeducativo

    # def calcularauxilioeducativo(self):
    #     auxilioeducativo = (0,05 * self.salario) * self.numeroHijos 
    #     return """Su Auxilio educativo es""" + auxilioeducativo

    def Consultarnumerohijos(self):
        return self.numeroHijos

    def cambiarsalario(self, nuevoSalario):
        # Aqui va el codigo del metodo cambiar salario
        return 0
    
    def cambiarEmpleado(self, nNombre, nApellido, nSexo, nSalario):
        # Aqui va sl codigo del nuevo empleado
        return None
    
    def ConsultarSalario(self):
        # Aqui va el codigo del metodo
        return self.salario
    
    def consultarNombre(self):
        # Aqui va el codigo del metodo
        return self.nombre
    
    def ConsultarApellido(self):
        # Aqui va el codigo del metodo
        return self.apellido
    
    def ConsultarNombreCompleto(self):
        # Aqui va el codgo del metodo
        return self.nombre +" "+ self.apellido
    
    def AumentoSalario(self):
        nSalario = self.salario * 0.05
        nSalario = nSalario + self.salario
        self.salario = nSalario
        return "El Nuevo Salario es de "+self.salario

    def Duplicarsalario(self):
        # Aqui va el codigo del metodo
        # self.salario=self.salario*2
        # este es la asignacion de la forma uno
        self.salario *=2

    def CalcularSalarioAnual(self):
        #Aqui va el codigo del metodo
        salarioanual= self.salario *12
        # return salarioanual
        # forma 2
        return self.salario*12
    
    def ConsultarDiaCumpleaños(self):
        return "El dia de su cumpleaños es"+self.fechanacimiento.ConsultarDia()
    
    def Calcularimpuesto(self):
        #Aqui
        total= self.CalcularSalarioAnual()
        return (total*19.5)/100
    
    def __init__(self, nombre, apellido, sexo, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.salario = salario
        
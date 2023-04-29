class Animal:
    def __init__(self, id, tipoH, nombreEspecie, nombreAnimal, tipoD, edad, sexo, tadaptacion, idTipoHan, tempDormir):
        self.idanimal = id
        self.tipoHabitad = tipoH
        self.nombreEspecie = nombreEspecie
        self.nombreAnimal = nombreAnimal
        self.tipoDieta = tipoD
        self.edad = edad
        self.sexoAnimal = sexo
        self.tipoAdap = tadaptacion
        self.idTipoHA = idTipoHan
        self.tempDormir = tempDormir
        
    def getIdAnimal(self):
        return self.idanimal
    
    def getTipoHabitad(self):
        return self.tipoHabitad
    
    def getNombreEspecie(self):
        return self.nombreEspecie
    
    def getNombreAnimal(self):
        return self.nombreAnimal
    
    def getTipoDieta(self):
        return self.tipoDieta
    
    def getedad(self):
        return self.edad
    
    def getSexoA(self):
        return self.sexoAnimal
    
    def getTipoAdapA(self):
        return self.tipoAdap
    
    def getIdTipoHA(self):
        return self.idTipoHA
    
    def setedad(self, newEdad):
        self.edad = newEdad
    
    def setIdAnimal(self, id):
        self.idanimal = id


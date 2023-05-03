from abc import ABC,abstractmethod 

class Animal(ABC):
    def __init__(self, idAnimal:int,edad:int,tipoH:int,tipoHabi:str, nombreEspecie:str,nombre:str,tipoDieta:int,horasD:int ,tem:tuple):
        self._idAnimal = idAnimal
        self._tipoHabitat = tipoH
        self._nombreEspecie = nombreEspecie
        self._nombreAnimal = nombre
        self._tipoDieta = tipoDieta
        self._adaptacion = None
        self._idAdaptacion = None
        self._tipoHabitatstr = tipoHabi
        self._horasDormir = horasD
        self._temA = tem
        self._boolDormir = False
        self._edad = edad
        self._boolJuego = False
        self._stComer = 0
        
    def getIdAnimal(self):
        return self._idAnimal

    def getIdTipoHA(self):
        return self._tipoHabitat

    def getTipoHabitad_str(self):
        return self._tipoHabitatstr
    
    def getNombreEspecie(self):
        return self._nombreEspecie
    
    def getNombreAnimal(self):
        return self._nombreAnimal
    
    def getTipoDieta(self):
        return self._tipoDieta
    
    def getedad(self):
        return self._edad

    def gethorasDormir(self):
        return self._horasDormir

    def getBoolDormir(self):
        return self._boolDormir

    def getBoolJuego(self):
        return self._boolJuego

    def getTuplaTemA(self):
        return self._temA

    def setTuplaTemA(self, newTupla: tuple):
        self._temA = newTupla
    
    def setEdad(self, newEdad:int):
        self._edad = newEdad

    def dormir(self):
        if self._boolDormir == False:
            self._boolDormir = True
            return "Esta muy cansado, va a dormir por " + str(self.gethorasDormir()) + "Horas."
        else:
            self.__boolDormir = False
            return "Esta muy activo, ya durmio sus "+ str(self.gethorasDormir()) + "Horas diarias."

    @abstractmethod
    def getTipoAdapA(self):
        pass

    @abstractmethod
    def getTipoAdapA_str(self):
        pass

    @abstractmethod
    def jugar(self):
        pass

    def Comer(self, alimentos, alimento):
    
        if ._tipoDieta == 1:
            
            if(alimentos.verificarCarnivoros(alimento,._idAdaptacion))
                alimentos.deleteAlimentoC(alimento,._idAdaptacion)
                print("Comiendo {alimento}...\n")

            else
                print("El alimento {alimento}, no se encuentra\n")
                
        elif ._tipoDieta == 2:

            if(alimentos.verificarHerbivoros(alimento,._idAdaptacion))
                alimentos.deleteAlimentoH(alimento,._idAdaptacion)
                print("Comiendo {alimento}...\n")

            else
                print("El alimento {alimento}, no se encuentra\n")

        elif ._tipoDieta == 3:

            
            if(alimentos.verificarCarnivoros(alimento,._idAdaptacion))
                alimentos.deleteAlimentoC(alimento,._idAdaptacion)
                print("Comiendo {alimento}...\n")

            elif(alimentos.verificarHerbivoros(alimento,._idAdaptacion))
                alimentos.deleteAlimentoH(alimento,._idAdaptacion)
                print("Comiendo {alimento}...\n")
             else
                print("El alimento {alimento}, no se encuentra\n")










from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self, idAnimal:int,edad:int,tipoH:int,tipoHabi:str, nombreEspecie:str,nombre:str,tipoDieta:int,horasD:int ):
        self._idAnimal = idAnimal
        self._tipoHabitat = tipoH
        self._nombreEspecie = nombreEspecie
        self._nombreAnimal = nombre
        self._tipoDieta = tipoDieta
        self._tipoHabitatstr = tipoHabi
        self._horasDormir = horasD
        self._boolDormir = False
        self._edad = edad
        self._boolJuego = False
        self._listaAlimentos = []
        
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

    def setEdad(self, newEdad:int):
        self._edad = newEdad

    def agregarAlimiento(self, newAlimento):
        try:
            self._listaAlimentos.append(newAlimento)
            if newAlimento in self._listaAlimentos == False:
                raise SystemError("Agregar alimento en lista")
            else:
                return 1
        except SystemError as e:
            return e


    def eliminarAlimento(self,nombreAlimento):
        indice,ban = 0,False
        try:
            for alimento in self._listaAlimentos:
                if alimento.getNombreAli == nombreAlimento:
                    temAlimento = self._listaAlimentos[indice]
                    del self._listaAlimentos[indice]

                    break

                indice+=1
            if ban == False:
                return 2 # No encontro Alimento
            else:
                if temAlimento in self._listaAlimentos == True:
                    raise SystemError("Eliminar alimento en lista")
                else:
                    return 1
        except SystemError as e:
            return e

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

    @abstractmethod
    def Comer(self):
        pass







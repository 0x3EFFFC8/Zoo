import Animal

class Habitat:
    def __init__(self, tipoH:str, id_tipo_h : int, tipo_dieta_ah:int, strTipoAdecuacionH:str, tipo_adecu_s:int, temperatura: tuple[int,int]):
        self.__tipoHabitad = tipoH # string
        self.__adecuacion = strTipoAdecuacionH # string
        self.__tipoAdecuacion = tipo_adecu_s # int
        self.__idTipoHabitad = id_tipo_h # int
        self.__tipoDietaAnimales = tipo_dieta_ah # int
        self.__cantidadAnimalesH = 0
        self.__vectoranimales = []
        self.__temperatura = temperatura

    def getTipoH_Str(self):
        return self.__tipoHabitad

    def getAdecuacion_Str(self):
        return self.__adecuacion

    def getIdTipoH(self):
        return self.__idTipoHabitad

    def getTipoDieta(self):
        return self.__tipoDietaAnimales
    def setTipoDieta(self, tipo):
        self.__tipoDietaAnimales = tipo

    def getTipoAdecuacion(self):
        return self.__tipoAdecuacion

    def setTipoAdecuacion(self, tipo):
        self.__tipoAdecuacion = tipo

    def getCantidadAH(self):
        return self.__cantidadAnimalesH

    def setCantidadAH(self, new_ca:int):
        if new_ca == 1:
            self.__cantidadAnimalesH += 1
        else:
            self.__cantidadAnimalesH -= 1

    def agregarAnimal(self, newAniamal:Animal ):
        pass

    def buscarEnHabitat(self, idA:int ):
        indice,ban = 0,False
        while indice < len(self.__vectoranimales) and ban == False:
            Animal = self.__vectoranimales[indice]
            if Animal.getIdAnimal() == idA:
                ban = True
            indice+=1
        if ban == True:
            return indice
        else:
            return -1
    def sacarAnimalH(self, idA:int ):
        indice = self.buscarEnHabitat(idA)
        if indice >= 0:
            try:
                temAnimal = self.__vectoranimales.pop(indice)
                if temAnimal in self.__vectoranimales == True:
                    raise SystemError("Sacar y eliminar del Vector")
                else:
                    self.setCantidadAH(-1)
                    return temAnimal
            except SystemError as e:
                return e
        else:
            return None
    def eliminarAnimal(self,idA:int ):
        indice = self.buscarEnHabitat(idA)
        if indice >= 0:
            animalT = self.__vectoranimales[indice]
            try:
                del self.__vectoranimales[indice]
                if  animalT in self.__vectoranimales == True:
                    raise SystemError("Eliminar del vector")
                else:
                    self.setCantidadAH(-1)
                    return 1
            except SystemError as e:
                return e
        else:
            return 0
    def retornarAnimal(self, idA:int):
        indice = self.buscarEnHabitat(idA)
        if indice >= 0:
            return self.__vectoranimales[indice]
        else:
            return None









 
    



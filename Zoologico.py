

import Habitat
import Animal



class Zoologico:
    def __init__(self,nombre:str):
        self.__nombreZ = nombre
        self._mapaHabitats: dict[int,Habitat] = {}
        self.__bodegaA: list[Animal] = []
        self.__totalH = 0
        self.__totalA = 0
        self.__creadorKeys = 0
        self.__creadorIds = 0

    def getNombre(self):
        return self.__nombreZ
    def getCreadorId(self):
        return self.__creadorIds
    def modiCreadorId(self):
        self.__creadorIds +=1

    def getCreadorKeys(self):
        return self.__creadorKeys
    def modiCreadorKey(self):
        self.__creadorKeys+=1

    def getTotalAZoo(self):
        return self.__totalA

    def setTotalAZoo(self, accion:int):
        if accion == 1:
            self.__totalA +=1
        else:
            self.__totalA-=1

    def getTotalHZoo(self):
        return self.__totalH
    def getMapa(self):
        return self._mapaHabitats
    def getBodega(self):
        return self.__bodegaA

    def setTotalHZoo(self, accion: int):
        if accion == 1:
            self.__totalH +=1
        else:
            self.__totalH -=1


    def agregarHabitat(self, newHabitat:Habitat):
        try:
            self._mapaHabitats[self.getCreadorKeys()] = newHabitat
            if self.getCreadorKeys() in self._mapaHabitats == False:
                raise IndexError("Fallo Ingreso en diccionario")
            else:
                self.modiCreadorKey()
                self.setTotalHZoo(1)
                return 1 # si el proceso salio bien

        except IndexError as e:
            return e # si el proceso falla

    def eliminarHabitat(self, keyBusqueda:int):

        if keyBusqueda in self._mapaHabitats == True:
            Habitat = self._mapaHabitats[keyBusqueda]
            if Habitat.getCantidadAH() == 0 :
                del self._mapaHabitats[keyBusqueda]
                self.setTotalHZoo(-1)
                return 1 # Encontro Habitat y esta vacio eliminación, se llevo a cabo la eliminacion
            else:
                return 2 #Hay Animales en el Habitat
        return 0 #No encontro el habitat

    def moverAnimal(self, keyHSalida, keyHentrada,idAnimal):
        banGeneral = 0
        banHSalida = keyHSalida in self._mapaHabitats
        banHEntrada = keyHentrada in self._mapaHabitats
        if banHEntrada == True and banHSalida == True:
            temHSalida = self._mapaHabitats[keyHSalida]
            temAnimal = temHSalida.retornarAnimal(idAnimal)
            if type(temAnimal) == Animal:
                temHllegada = self._mapaHabitats[keyHentrada]
                banProcesoIngreso =  temHllegada.agregarAnimalH(temAnimal)
                if banProcesoIngreso == 1:
                    temHllegada.setCantidadAH(1)
                    temHSalida.setCantidadAH(-1)
                    banGeneral = 1
                else:
                    banGeneral = banProcesoIngreso
            else:
                banGeneral = -7 # El animal no fue encontrado dentro del Habitat de salida
        else:
            if banHEntrada == False and banHSalida == False:
                banGeneral = -8 # Los 2 habitats no fueron encontrados
            elif banHSalida == False:
                banGeneral = -9 # El habitat de Salida no fue encontrado
            else:
                banGeneral = -10 # El habitat de llegada no fue encontrado
        return banGeneral

    def agregarAnimalBodega(self, newAnimal:int):
        self.__bodegaA.append(newAnimal)
        self.setTotalAZoo(1)


    def animalEnBodega(self,idA):
        indice = 0
        tamBodega = len(self.__bodegaA)
        if tamBodega >0:
            ban = False
            while indice < tamBodega and ban == False:
                temAnimal = self.__bodegaA[indice]
                if temAnimal.getIdAnimal() == idA:
                    ban == True
                else:
                    indice+=1
            if ban == False:
                indice = -1

        else:
            indice = -1
        return indice
    def sacarAnimalBodega(self, idAnimal:int):

        indice = self.animalEnBodega(idAnimal)
        if indice >=0:
            return self.__bodegaA.pop(indice)
        else:
            return None
    def eliminarAnimalBodega(self, idAnimal: int):
        indice = self.animalEnBodega(idAnimal)
        if indice>=0:
            try:
                del self.__bodegaA[indice]
                if self.animalEnBodega(idAnimal) == -1:
                    ban = 1 # procesoExitoso
                else:
                    raise SystemError("Eliminar en Bodega")

            except SystemError as e:
                return e # retorna el eror
        else:
            ban = -1 # no se encontro animal
        return ban













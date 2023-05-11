

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
            return e.args # si el proceso falla

    def eliminarHabitat(self, keyBusqueda:int):

        if keyBusqueda in self._mapaHabitats == True:
            Habitat = self._mapaHabitats[keyBusqueda]
            if Habitat.getCantidadAH() == 0 :
                del self._mapaHabitats[keyBusqueda]
                self.setTotalHZoo(-1)
                return 1 # Encontro Habitat y esta vacio eliminación, se llevo a cabo la eliminacion
            else:
                return "Hay Animales en el Habitat.\nNo Es Posible Eliminar"
        return "No se encontro el habitat en el Zoologico"

    def agregarAnimalBodega(self, newAnimal:int):
        self.__bodegaA.append(newAnimal)
        self.setTotalAZoo(1)


    def animalEnBodega(self,idA):
        indice = 0
        tamBodega = len(self.__bodegaA)
        if tamBodega > 0:
            ban = False
            while indice < tamBodega and ban == False:
                temAnimal = self.__bodegaA[indice]
                if temAnimal.getIdAnimal() == idA:
                    ban = True
                    return indice
                else:
                    indice+=1
            if ban == False:
                return "No se encontro Animal en la Bodega"

        else:
            return "No Hay animales en la Bodega"
    def sacarAnimalBodega(self, idAnimal:int):

        indice = self.animalEnBodega(idAnimal)
        if indice >=0:
            return self.__bodegaA.pop(indice)
        else:
            return None
    def eliminarAnimalBodega(self, idAnimal: int):
        indice = self.animalEnBodega(idAnimal)
        ban = None
        if indice>=0:
            try:
                del self.__bodegaA[indice]
                if self.animalEnBodega(idAnimal) == -1:
                    self.setTotalAZoo(-1)
                    ban = 1 # procesoExitoso
                else:
                    raise SystemError("Eliminar en Bodega")

            except SystemError as e:
                return e.args # retorna el error
        else:
            ban = indice
        return ban
    def agregarAnimalH(self, animalB : Animal , idHabitat : int):
        banHabitat = idHabitat in self._mapaHabitats
        banGeneral = 0
        if banHabitat:
            banIngreso = self._mapaHabitats[idHabitat].agregarAnimalH(animalB)
            if banIngreso == 1:
                self._mapaHabitats[idHabitat].setCantidadAH(1)
                banGeneral = 1
            else:
                banGeneral = banIngreso
        else:
            banGeneral = "Habitat De llegada no encontrado"
        return banGeneral
    def retornarAnimalBodega(self, indA:int):
        return self.__bodegaA[indA]














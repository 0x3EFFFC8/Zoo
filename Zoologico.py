
class Zoologico:
    def __init__(self,nombre):
        self.__nombreZ = nombre
        self._mapaHabitads = {}
        self.__bodegaA = []
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

    def setTotalAZoo(self, accion):
        if accion == 1:
            self.__totalA +=1
        else:
            self.__totalA-=1

    def getTotalHZoo(self):
        return self.__totalH

    def setTotalHZoo(self, accion):
        if accion == 1:
            self.__totalH +=1
        else:
            self.__totalH -=1

    def agregarHabitat(self, newHabitat):
        self._mapaHabitads[self.getCreadorKeys()] = newHabitat
        self.modiCreadorKey()

    def buscarHabitat(self, keyH):
        ban = False
        for key in self._mapaHabitads:
            if key == keyH:
                ban = True
                break
        return ban






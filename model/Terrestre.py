import Animal
class Terrestre(Animal):
    def __init__(self,idAnimal:int,edad:int,tipoH:int,tipoHabi:str, nombreEspecie:str,nombre:str,tipoDieta:int,horasD:int ):
        super().__init__(idAnimal,edad,tipoH,tipoHabi, nombreEspecie,nombre,tipoDieta,horasD )
        self._adaptacion = "Terrestre"
        self._idAdaptacion = 1

    def getTipoAdapA(self):
        super().getTipoAdapA()
        return self._idAdaptacion

    def getTipoAdapA_str(self):
        super().getTipoAdapA_str()
        return self._adaptacion

    def jugar(self):
        super().jugar()
        if self._boolJuego == False:
            self._boolJuego = True
            return "Corre y juega muy feliz"
        else:
            self._boolJuego = False
            return "Esta Cansado de Jugar, se fue a descansar."


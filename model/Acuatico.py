import model.Animal
class Acuatico(model.Animal.Animal):
    def __init__(self, idAnimal: int, edad: int, tipoH: int, tipoHabi: str, nombreEspecie: str, nombre: str,tipoDieta: int, horasD:int,temA:tuple ):
        super().__init__(idAnimal, edad, tipoH, tipoHabi, nombreEspecie, nombre, tipoDieta, horasD,temA)
        self._adaptacion = "Acuatico"
        self._idAdaptacion = 2

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
            return "Nada por todo el acuario, muy rapido."

        else:
            self._boolJuego = False
            return "Esta Cansado, esta nadando lento."

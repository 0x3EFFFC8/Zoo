import model.Animal
class Volador(model.Animal.Animal):
    def __init__(self, idAnimal: int, edad: int, tipoH: int, tipoHabi: str, nombreEspecie: str, nombre: str,tipoDieta: int, horasD: int, temA:tuple):
        super().__init__(idAnimal, edad, tipoH, tipoHabi, nombreEspecie, nombre, tipoDieta, horasD,temA)
        self._adaptacion = "Volador"
        self._idAdaptacion = 4

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
            return "Vuela por todo el recinto, esta muy animado."
        else:
            self._boolJuego = False
            return "Esta Cansado de jugar esta posado en su lugar favorito."

import view.viewZologico
import model.Zoologico
import model.Habitat
import model.Animal
import model.Volador
import model.Acuatico
import model.SemiAcuatico
import model.Terrestre
class controllerZoo:
    def __init__(self, zooA:model.Zoologico,temAnimal:model.Animal,temHabitat:model.Habitat,viewZoo:view.viewZologico):
        self._Zoologico = zooA
        self.temAnimal = temAnimal
        self.temHabitat = temHabitat
        self._viewZologico = viewZoo
        self._dicTipoH = {1:"Selvatico" , 2:"Bosque", 3: "Desertico",4: "Oceanico",5:"Polar",6: "Manglar",7:"Montañoso",8:"Tropical" ,9:"Sabana"}
        self._dicAdecuacion = {1:"Terrestre" , 2:"Acuatico", 3: "SemiAcuatico",4: "Volador"}

    def recibirOpcion(self,res):
        try:
            if res.isdigit() == True:
                res = int(res)
                return res
            else:
                raise TypeError("Solo se aceptan valores enteros")
        except TypeError as e:
            return e

    def crearHabitat(self):
        resU = ""
        error = ""
        print("Ingres el tipo de Adecuacion del Habitat")
        self._viewZologico.panelAdecuacion()
        opcAde = self.recibirOpcion(input())
        print("Ingres el tipo del Habitat")
        self._viewZologico.panelTipoHabitat()
        opcTipoH = self.recibirOpcion(input())
        print("Ingrese el tipo de dieta")
        self._viewZologico.panelDieta()
        opcDieta = self.recibirOpcion(input())
        print("Ingrese los datos de la temperatura del habitat")
        opcionesTem = [0, 0]
        opcionesTem[0] = self.recibirOpcion(input("Ingrese la tempereratura Min: "))
        opcionesTem[1] = self.recibirOpcion(input("Ingrese la tempereratura Max: "))

        if type(opcAde) == int and type(opcTipoH) == int and type(opcDieta) == int and type(opcionesTem[0]) == int and type(opcionesTem[1]== int):
            if opcAde > 0 and opcAde <= 4:
                if opcTipoH > 0 and opcTipoH <= 9:
                    if opcDieta >0 and opcDieta <= 3:
                        if opcionesTem[0] < opcionesTem[1]:
                            self.temHabitat = model.Habitat(self._dicTipoH[opcTipoH], opcTipoH, opcDieta, self._dicAdecuacion[opcAde], opcAde, opcionesTem)
                            res = self._Zoologico.agregarHabitat(self.temHabitat)
                            if res != 1:
                                 error = res.args
                        else:
                            error = "Los Valores de la tem min deben ser menores que los de la tem maxima"
                    else:
                        error = "Dieta invalida o vale 0 "
                else:
                     error = "opcion tipo habitat o vale 0"
            else:
                error = "opcion Adecuaciono o valio 0"
        else:
            error = "Ingreso Solo de Enteros, se detectaron caracteres"

        if error == "":
            resU = "Proceso Exitoso."
            print(resU)
        else:
            resU = "Error: "
            print(resU, error)
    def menuZoo(self):
        ban = True
        while ban:
            self._viewZologico.menuZoologico(self._Zoologico)
            opc = self.recibirOpcion(input())
            if type(opc) == int:
                self._viewZologico.mostrarTituloMenuP(opc)
                if opc == 0:
                    ban = False
                elif opc == 1:
                    self._viewZologico.mostrarHabitats(self._Zoologico)
                elif opc == 2:
                    self.crearHabitat()
                elif opc == 3:
                    pass
                elif opc == 4:
                    pass
                elif opc == 5:
                    pass
                elif opc == 6:
                    pass
            else:
                print("Se ha Generado un Error: ", opc.args)





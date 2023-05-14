import view.viewZologico as viewZoo
import model.Zoologico as ZoologicoM
import model.Habitat as HabitatM
import model.Animal as AnimalM
import model.Alimento as AlimientoC
import model.Volador
import model.Acuatico
import model.SemiAcuatico
import model.Terrestre
import model.Alimento

import streamlit as st
class controllerZoo:
    def __init__(self):
        self._ZoologicoC = ZoologicoM.Zoologico("ZOOLOGICO DE CALI")
        self.temAnimal = None
        self.temHabitat = None
        self._viewZologico = viewZoo.viewZoologico()
        self._alimientosZ = AlimientoC.Alimento()
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
            return e.args

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
                                 error = res
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
    def eliminarHabitat(self):
        # Mostrar Habitats
        resU = ""
        error = ""
        keyH = self.recibirOpcion(input("Ingrese Clave del Habitat"))
        if type (keyH) == int:
            resProceso = self._ZoologicoC.eliminarHabitat(keyH)
            if resProceso != 1:
                error = resProceso
        else:
            error = keyH
        if error == "":
            resU = "EL HABITAT "+ str(keyH) + ".\nFue eliminado del Zoologico con Exito"
        else:
            resU = "Error"

    def subMenuBodega(self):
        pass
    def submenuHabitat(self):

        sub_menuH = ["Agregar Animal al habitat", "Sacar Animal del Zoologico", "Mostrar Animales dentro del habitat", "Interactuar Animal"]
        eleccionH = st.sidebar.selectbox("Seleccione una opción", sub_menuH)
        # Mostrar contenido según la opción del submenú seleccionada
        if eleccionH == "Agregar Animal al habitat":
            st.write("Agregando")
        elif eleccionH == "Mostrar Animales dentro del habitat":
            pass
        elif eleccionH == "Sacar Animal del Zoologico":
            st.write("Contenido de la opción 2 de Opciones")
        elif eleccionH == "Interactuar Animal":
            st.write("Contenido de la opción 3 de Opciones")

    def menuZoo(self):
        menu = ["Ver Mapa Zoologico", "Crear Habitat", "Ver Habitat", "Eliminar Habitat del Zoologico", "Bodega"]
        eleccionMenu = st.sidebar.selectbox("Seleccione una opción", menu)

        if eleccionMenu == "Ver Mapa Zoologico":
            st.write("Contenido de la opción Inicio")
        elif eleccionMenu == "Crear Habitat":
            pass
        elif eleccionMenu == "Ver Habitat":
            pass
        elif eleccionMenu == "Eliminar Habitat del Zoologico":
            pass
        elif eleccionMenu == "Bodega":
            pass





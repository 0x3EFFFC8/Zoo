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

    """
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

    """
    def subMenuBodega(self):
        pass
    def submenuHabitat(self):

        sub_menuH = ["Agregar Animal al habitat", "Sacar Animal del Zoologico", "Mostrar Animales dentro del habitat", "Interactuar Animal"]
        eleccionH = st.sidebar.radio("Selecciona una opción", sub_menuH)

        # Crear el submenú horizontal

        if eleccionH == "Agregar Animal al habitat":
            st.write("Agregando")
        elif eleccionH == "Mostrar Animales dentro del habitat":
            pass
        elif eleccionH == "Sacar Animal del Zoologico":
            st.write("Contenido de la opción 2 de Opciones")
        elif eleccionH == "Interactuar Animal":
            st.write("Contenido de la opción 3 de Opciones")

    def menuZoo(self):
        st.markdown(f"<h1 style='text-align: center; color: green;font-family: Times New Roman;margin-top: -50px;background-color: #d9f2c3;'>{self._ZoologicoC.getNombre()}</h1>", unsafe_allow_html=True)

        menu = ["Ver Mapa Zoologico", "Crear Habitat", "Ver Habitat", "Eliminar Habitat del Zoologico", "Bodega"]
        eleccionMenu = st.sidebar.selectbox("Seleccione una opción", menu)
        """
        botones_container = st.container()
        botones_container.markdown("<p style='margin-top: 100px;'></p>", unsafe_allow_html=True)

        # Agregar columnas para los botones y el contenido principal
        col1, col2 , col3= st.columns(3)

        # Agregar texto a la primera columna
        with col1:
            st.write("<h1 style='text-align: center; font-family: Arial; font-size: 10px;'>Título centrado en Arial</h1>", unsafe_allow_html=True)
        with col2:
            st.write(' La Otra Col')
        with col3:
            st.write('Era col')

        # Agregar botones en el contenedor de botones
        with botones_container:
            st.button('Botón 1')
            st.button('Botón 2')

        # Agregar contenido principal en la segunda columna
        with col2:
            st.write('¡Hola! Bienvenido a mi aplicación.')
        """
        if eleccionMenu == "Ver Mapa Zoologico":
            self._viewZologico.mostrarHabitats(self._ZoologicoC.getMapa(),self._ZoologicoC.getTotalAZoo(),self._ZoologicoC.getTotalHZoo())

        elif eleccionMenu == "Crear Habitat":
            tuplaT = None

            columnas = st.columns(3)
            listaInfo =self._viewZologico.paneles(columnas)
            with columnas[2]:
                minT = st.slider('Temperatura Min ', -20, 34, 10)
                maxT = st.slider('Temperatura Max', -19, 35, 25)
                if minT > maxT:
                    st.info("Valores invalidos")
                elif minT == maxT:
                    st.info("Las temperatura no pueden ser iguales")
                else:
                    tuplaT = (minT,maxT)
            st.write(listaInfo[0],listaInfo[1],listaInfo[2])
            with columnas[0]:
                envio = st.button("Crea Habitat")
                if tuplaT != None and envio == True:
                    self.temHabitat = HabitatM.Habitat(self._dicTipoH[listaInfo[2]],listaInfo[2],listaInfo[1],self._dicAdecuacion[listaInfo[0]],listaInfo[0],tuplaT)
                    resIngre = self._ZoologicoC.agregarHabitat(self.temHabitat)
                    if resIngre == 1:
                        st.success("Habitat Ingresado Correctamente")
                    else:
                        st.error(resIngre)

        elif eleccionMenu == "Ver Habitat":
             self.submenuHabitat()
        elif eleccionMenu == "Eliminar Habitat del Zoologico":
            if self._ZoologicoC.getTotalHZoo() > 0:
                dicInverso = {}
                mapa = self._ZoologicoC.getMapa()
                for habitatId in mapa:
                    temH:model.Habitat.Habitat = mapa[habitatId]
                    newClave = str(habitatId) + " - " + temH.getAdecuacion_Str() +" - "+ temH.getAdecuacion_Str()
                    dicInverso[newClave] = habitatId
                cajaHabitats = st.selectbox("Elige una opción", list(dicInverso.keys()))
                eleccion = dicInverso[cajaHabitats]
                botonE = st.button("ELIMINAR")
                self._viewZologico.mostrarHabitats(self._ZoologicoC.getMapa(), self._ZoologicoC.getTotalAZoo(),
                                                   self._ZoologicoC.getTotalHZoo())

                if botonE == True:
                    resProceso = self._ZoologicoC.eliminarHabitat(eleccion)
                    if resProceso == 1:
                        st.success("El Habitat seleccionado fue eliminado.\nCorrectamente")
                    else:
                        st.error(resProceso)
            else:
                st.info("NO HAY HABITATS EN EL ZOOLOGICO")




        elif eleccionMenu == "Bodega":
            pass





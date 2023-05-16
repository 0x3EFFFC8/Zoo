import view.viewZologico as viewZoo
import model.Zoologico as ZoologicoM
import model.Habitat as HabitatM
import model.Animal as AnimalM
import model.Alimento as AlimientoC
import model.Volador as VoladorM
import model.Acuatico as AcuaticoM
import model.SemiAcuatico as SemiAcuaticoM
import model.Terrestre as TerrestreM
import model.Alimento as AlimentoM

import streamlit as st
class controllerZoo:
    def __init__(self):

        if "Zoologico" in st.session_state:
            self._ZoologicoC = st.session_state["Zoologico"]
        else:
            self._ZoologicoC = ZoologicoM.Zoologico("ZOOLOGICO DE CALI")

        self.temAnimal = None
        self.temHabitat = None
        self._viewZologico = viewZoo.viewZoologico()
        self._alimientosZ = AlimientoC.Alimento()
        self._dicTipoH = {1:"Selvatico" , 2:"Bosque", 3: "Desertico",4: "Oceanico",5:"Polar",6: "Manglar",7:"Montañoso",8:"Tropical" ,9:"Sabana"}
        self._dicAdecuacion = {1:"Terrestre" , 2:"Acuatico", 3: "SemiAcuatico",4: "Volador"}

    """


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
    def tieneNumeros(string):
        return any(char.isdigit() for char in string)
    def panelCrearAnimalHabitat(self, habitatAde,habitatDie,habitatTipo):
        tuplaT = None
        nombre = None
        especie = None
        edad = None
        horasS = None
        columnas = st.columns(3)
        with columnas[0]:
            nombre = st.text_input('Nombre del animal: ')
            edad = st.slider('Edad', 1, 27, 5)
        with columnas[1]:
            especie = st.text_input("Nombre especie:")
            horasS = st.slider('Horas de Descanso del Animal', 1, 14, 7)
        with columnas[2]:
            minT = st.slider('Temperatura Min', -20, 34, 10)
            maxT = st.slider('Temperatura Max', -19, 35, 25)
            if minT > maxT:
                st.info("Valores invalidos")
            elif minT == maxT:
                st.info("Las temperatura no pueden ser iguales")
            else:
                tuplaT = (minT, maxT)
        with columnas[0]:
            if nombre.isalpha() == False :
                st.info("El Nombre debe tener solo Caracteres Alfabeticos")
            elif especie.isalpha() == False:
                st.info("El Nombre de la especie debe tener solo Caracteres Alfabeticos")
            envio = st.button("Agrega Animal")
            if tuplaT != None and envio == True:
                nombre = nombre.lower()
                especie = especie.lower()
                temAnimal: AnimalM = None
                if habitatAde == 1:
                    temAnimal = TerrestreM.Terrestre(self._ZoologicoC.getCreadorId(), edad, habitatTipo,
                                                     self._dicTipoH[habitatTipo], especie, nombre, habitatDie,
                                                     horasS,tuplaT)
                elif habitatAde == 2:
                    temAnimal = AcuaticoM.Acuatico(self._ZoologicoC.getCreadorId(), edad, habitatTipo,
                                                     self._dicTipoH[habitatTipo], especie, nombre, habitatDie,
                                                     horasS,tuplaT)
                elif habitatAde == 3:
                    temAnimal = SemiAcuaticoM.SemiAcuatico(self._ZoologicoC.getCreadorId(), edad, habitatTipo,
                                                     self._dicTipoH[habitatTipo], especie, nombre, habitatDie,
                                                     horasS,tuplaT)
                else:
                    temAnimal = VoladorM.Volador(self._ZoologicoC.getCreadorId(), edad, habitatTipo,
                                                     self._dicTipoH[habitatTipo], especie, nombre, habitatDie,
                                                     horasS,tuplaT)
                return temAnimal
            else:
                return None
    def panelcrearAnimalBodega(self):
        tuplaT = None
        nombre = None
        especie = None
        edad = None
        horasS = None
        columnas = st.columns(3)
        with columnas[0]:
            nombre = st.text_input('Nombre del animal: ')
        with columnas[1]:
            especie = st.text_input("Nombre especie:")
        listaInfo = self._viewZologico.paneles(columnas)
        with columnas[2]:
            edad = st.slider('Edad', 1, 27, 5)
            minT = st.slider('Temperatura Min', -20, 34, 10)
            maxT = st.slider('Temperatura Max', -19, 35, 25)
            horasS = st.slider('Horas de Descanso del Animal', 1, 14, 7)
            if minT > maxT:
                st.info("Valores invalidos")
            elif minT == maxT:
                st.info("Las temperatura no pueden ser iguales")
            else:
                tuplaT = (minT, maxT)
        st.write(listaInfo[0], listaInfo[1], listaInfo[2])
        with columnas[0]:
            envio = st.button("Agrega Animal")
            if nombre.isalpha() == False :
                st.info("El Nombre debe tener solo Caracteres Alfabeticos")
            elif especie.isalpha() == False:
                st.info("El Nombre de la especie debe tener solo Caracteres Alfabeticos")
            if tuplaT != None and envio == True:
                nombre = nombre.lower()
                especie = especie.lower()
                adecuacion = listaInfo[0]
                temAnimal:AnimalM = None
                if adecuacion == 1:
                    temAnimal = TerrestreM.Terrestre(self._ZoologicoC.getCreadorId(), edad, listaInfo[2],
                                                          self._dicTipoH[listaInfo[2]], especie, nombre, listaInfo[1],
                                                          horasS, tuplaT)
                elif adecuacion == 2:
                    temAnimal = AcuaticoM.Acuatico(self._ZoologicoC.getCreadorId(), edad, listaInfo[2],
                                                        self._dicTipoH[listaInfo[2]], especie, nombre, listaInfo[1],
                                                        horasS, tuplaT)
                elif adecuacion == 3:
                    temAnimal = SemiAcuaticoM.SemiAcuatico(self._ZoologicoC.getCreadorId(), edad, listaInfo[2],
                                                                self._dicTipoH[listaInfo[2]], especie, nombre,
                                                                listaInfo[1], horasS, tuplaT)
                else:
                    temAnimal = VoladorM.Volador(self._ZoologicoC.getCreadorId(), edad, listaInfo[2],
                                                      self._dicTipoH[listaInfo[2]], especie, nombre, listaInfo[1],
                                                    horasS, tuplaT)
                return temAnimal
            else:
                return None
    def submenuHabitat(self, habitatI : HabitatM.Habitat, keyH:int):
            contenedor = st.container()
            with contenedor:
                st.title("*** |  Bienvenido al Habitat "+ str(keyH)+ " " + habitatI.getTipoH_Str()+ " | ***")
                st.title("** |   Adecuado para especies de tipo " + habitatI.getAdecuacion_Str())
            sub_menuH = ["Agregar Animal al habitat", "Sacar Animal del Zoologico", "Mostrar Animales dentro del habitat", "Interactuar Animal"]
            eleccionH = st.sidebar.selectbox("Selecciona una opción", sub_menuH)
            # Crear el submenú horizontal
            if eleccionH == "Agregar Animal al habitat":
                ingresoAnimal = self.panelCrearAnimalHabitat(habitatI.getTipoAdecuacion(),habitatI.getTipoDieta(),habitatI.getIdTipoH())
                if type(ingresoAnimal) == AnimalM.Animal:
                    resIngre = habitatI.agregarAnimalH(ingresoAnimal)
                    if resIngre == 1:
                        st.session_state["Zoologico"] = self._ZoologicoC
                        st.success("Animal Ingresado Correctamente en el Habitat")
                    else:
                        st.error(resIngre)
            elif eleccionH == "Mostrar Animales dentro del habitat":
                pass
            elif eleccionH == "Sacar Animal del Zoologico":
                st.write("Contenido de la opción 2 de Opciones")
            elif eleccionH == "Interactuar Animal":
                st.write("Contenido de la opción 3 de Opciones")
    def subMenuBodega(self):
        sub_menuT = ["Agregar Animal", "Eliminar Animal", "Mover a Habitat",
                     "Mostrar Bodega"]
        eleccionB = st.sidebar.selectbox("Selecciona una opción", sub_menuT)
        # Crear el submenú horizontal
        st.markdown("<h1 style='text-align: center; color: #6495ED; font-family: Palatino, serif;'>[-- Bienvenido a la Bodega --]</h1>", unsafe_allow_html=True)
        if eleccionB == "Agregar Animal":
            ingresoAnimal: AnimalM.Animal = self.panelcrearAnimalBodega()
            if ingresoAnimal != None:
                resIngre = self._ZoologicoC.agregarAnimalBodega(ingresoAnimal)
                if resIngre == 1:
                    st.session_state["Zoologico"] = self._ZoologicoC
                    st.success("Animal Ingresado Correctamente en la Bodega")
                else:
                    st.error(resIngre)
        elif eleccionB == "Eliminar Animal":
            pass
        elif eleccionB == "Mover a Habitat":
            pass
        elif eleccionB == "Mostrar Bodega":
            pass
    def menuZoo(self):
        st.markdown(f"<h1 style='text-align: center; color: green;font-family: Times New Roman;margin-top: -50px;background-color: #d9f2c3;'>{self._ZoologicoC.getNombre()}</h1>", unsafe_allow_html=True)
        menu = ["Ver Mapa Zoologico", "Crear Habitat", "Ver Habitat", "Eliminar Habitat del Zoologico", "Bodega"]
        eleccionMenu = st.sidebar.selectbox("Seleccione una opción", menu)
        if eleccionMenu == "Ver Mapa Zoologico":
            mapa = self._ZoologicoC.getMapa()
            totalA = self._ZoologicoC.getTotalAZoo()
            totalH = self._ZoologicoC.getTotalHZoo()
            self._viewZologico.mostrarHabitats(mapa,totalA,totalH)
        elif eleccionMenu == "Crear Habitat":
            tuplaT = None
            columnas = st.columns(3)
            listaInfo = self._viewZologico.paneles(columnas)
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
                        st.session_state["Zoologico"] = self._ZoologicoC
                        st.success("Habitat Ingresado Correctamente")
                    else:
                        st.error(resIngre)
        elif eleccionMenu == "Ver Habitat":
            dicInverso = {}
            mapa = self._ZoologicoC.getMapa()
            if self._ZoologicoC.getTotalHZoo() == 0:
                caja = st.selectbox("No Hay Habitats en el Zoologico",["VACIO"])
            else:
                for key in mapa:
                    temH: HabitatM.Habitat = mapa[key]
                    newClave = str(key) + " - " + temH.getAdecuacion_Str() + " - " + temH.getTipoH_Str()
                    dicInverso[newClave] = key
                cajaHabitats = st.selectbox("Elige el Habitat al que deceas ingresar:", list(dicInverso.keys()))
                eleccion = dicInverso[cajaHabitats]
                botonE = st.button("Ingresar")
                st.write(eleccion)

                self.submenuHabitat(self._ZoologicoC.getMapa()[eleccion], eleccion)

        elif eleccionMenu == "Eliminar Habitat del Zoologico":
            if self._ZoologicoC.getTotalHZoo() > 0:
                dicInverso = {}
                mapa = self._ZoologicoC.getMapa()
                for key in mapa:
                    temH:HabitatM.Habitat = mapa[key]
                    newClave = str(key) + " - " + temH.getAdecuacion_Str() +" - "+ temH.getTipoH_Str()
                    dicInverso[newClave] = key
                cajaHabitats = st.selectbox("Elige una opción", list(dicInverso.keys()))
                eleccion = dicInverso[cajaHabitats]
                botonE = st.button("ELIMINAR")
                if botonE == True:
                    resProceso = self._ZoologicoC.eliminarHabitat(eleccion)
                    st.write(resProceso)
                    if resProceso == 1:
                        st.session_state["Zoologico"] = self._ZoologicoC
                        st.success("El Habitat seleccionado fue eliminado.\nCorrectamente")
                    else:
                        st.error(resProceso)
            else:
                st.info("NO HAY HABITATS EN EL ZOOLOGICO")
        elif eleccionMenu == "Bodega":
            self.subMenuBodega()

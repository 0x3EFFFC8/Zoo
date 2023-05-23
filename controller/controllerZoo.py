import view.viewZologico as viewZoo
import model.Zoologico as ZoologicoM
import model.Habitat as HabitatM
import model.Animal as AnimalM
import model.Volador as VoladorM
import model.Acuatico as AcuaticoM
import model.SemiAcuatico as SemiAcuaticoM
import model.Terrestre as TerrestreM
import model.Alimento as AlimentoC
import requests
import streamlit as st
import os
import time
import threading

class controllerZoo:
    def __init__(self):

        if "Zoologico" in st.session_state:
            self._ZoologicoC = st.session_state["Zoologico"]
        else:
            self._ZoologicoC = ZoologicoM.Zoologico("ZOOLOGICO JAVE-PAVO")
        if "comida" in st.session_state:
            self._AlimentoM = st.session_state["comida"]
        else:
            self._AlimentoM = AlimentoC.Alimento()
        self.temAnimal = None
        self.temHabitat = None
        self._viewZoologico = viewZoo.viewZoologico()
        self._dicTipoH = {1:"Selvatico" , 2:"Bosque", 3: "Desertico",4: "Oceanico",5:"Polar",6: "Manglar",7:"Montañoso",8:"Tropical" ,9:"Sabana"}
        self._dicAdecuacion = {1:"Terrestre" , 2:"Acuatico", 3: "SemiAcuatico",4: "Volador"}

    def cronometro(self,tiempo):
        hilo = threading.Thread(target=self.cronometro, args=(tiempo))
        hilo.start()
        time.sleep(tiempo)
        hilo.join()
        st.experimental_rerun()


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
                temAnimal: AnimalM.Animal = None
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
        listaInfo = self._viewZoologico.paneles(columnas)
        with columnas[2]:
            edad = st.slider('Edad', 1, 27, 5)
            minT = st.slider('Temperatura Min', -20, 34, 10)
            maxT = st.slider('Temperatura Max', -19, 35, 25)
            horasS = st.slider('Horas de Descanso del Animal', 1, 16, 7)
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
            st.title("* |  Bienvenido al Habitat "+ str(keyH)+ " " + habitatI.getTipoH_Str()+ " | ***")
            st.title("** |  Adecuado para especies de tipo " + habitatI.getAdecuacion_Str()  +" con una dieta "+ self._viewZoologico.dicDieta[habitatI.getTipoDieta()])
            st.title("*** |  Temperatura del Habitat "+ str(habitatI.getTuplaTemH()[0])+"/" +str(habitatI.getTuplaTemH()[1])+" Cº")
        sub_menuH = ["Agregar Animal al habitat", "Sacar Animal del Zoologico", "Mostrar Animales dentro del habitat","Sacar Habitat a Bodega", "Interactuar Animal"]
        eleccionH = st.sidebar.selectbox("Selecciona una opción", sub_menuH)
        # Crear el submenú horizontal
        if eleccionH == "Agregar Animal al habitat":
            ingresoAnimal = self.panelCrearAnimalHabitat(habitatI.getTipoAdecuacion(),habitatI.getTipoDieta(),habitatI.getIdTipoH())

            if ingresoAnimal != None:
                resIngre = habitatI.agregarAnimalH(ingresoAnimal)
                if resIngre == 1:
                    self._ZoologicoC.setTotalAZoo(1)
                    self._ZoologicoC.modiCreadorId()
                    st.session_state["Zoologico"] = self._ZoologicoC
                    st.success("Animal Ingresado Correctamente en el Habitat")
                else:
                    st.error(resIngre)
                self.cronometro(5)
        elif eleccionH == "Mostrar Animales dentro del habitat":
            self._viewZoologico.mostrarAnimalesHabitat(habitatI,keyH)
        elif eleccionH == "Sacar Animal del Zoologico":
            if habitatI.getCantidadAH() > 0:
                idAnimal = None
                dicInversoA = {"": 0}
                listAnimalesH: list[AnimalM.Animal] = habitatI.getVectorAH()
                for animalE in listAnimalesH:
                    tuplaTa = animalE.getTuplaTemA()
                    newValA = animalE.getIdAnimal()
                    newClaveA = animalE.getNombreAnimal()+" - "+animalE.getNombreEspecie() + " - " + animalE.getTipoAdapA_str() + " - " + animalE.getTipoHabitad_str() + " - Tem[" + str(tuplaTa[0]) + "/" + str(tuplaTa[1]) + "]"
                    dicInversoA[newClaveA] = newValA
                cajaElecAnimalesH = st.selectbox("Elige un Animal: ", list(dicInversoA.keys()))
                idAnimalH = dicInversoA[cajaElecAnimalesH]
                if cajaElecAnimalesH!= 0:
                    botonAB = st.button("Sacar Animal")
                    if botonAB == True:
                        proceso = habitatI.eliminarAnimal(idAnimalH)
                        if proceso == 1:
                            self._ZoologicoC.setTotalAZoo(-1)
                            st.success("El animal fue Trasladado fuera del Zoologico con Exito.")
                            st.session_state["Zoologico"] = self._ZoologicoC
                        else:
                            st.error(proceso)
                        self.cronometro(5)


        elif eleccionH == "Sacar Habitat a Bodega":
            ## Mirar porque no funciona
            if habitatI.getCantidadAH() > 0:
                idAnimal = None
                dicInversoAM = {"": 0}
                listAnimalesHM: list[AnimalM.Animal] = habitatI.getVectorAH()
                for animalE in listAnimalesHM:
                    newValA = animalE.getIdAnimal()
                    newClaveA = animalE.getNombreAnimal()+" - "+animalE.getNombreEspecie() + " - " + animalE.getTipoAdapA_str() + " - " + animalE.getTipoHabitad_str() + " - Edad" + str(animalE.getedad())
                    dicInversoAM[newClaveA] = newValA
                cajaElecAnimalesHM = st.selectbox("Elige un Animal: ", list(dicInversoAM.keys()))
                idAnimalHM = dicInversoAM[cajaElecAnimalesHM]
                if cajaElecAnimalesHM != 0:
                    botonAB = st.button("Mover a Bodega")
                    if botonAB == True:
                        animalT : AnimalM.Animal = habitatI.sacarAnimalH(idAnimalHM)
                        if type(animalT) != str:
                            proceso = self._ZoologicoC.agregarAnimalBodega(animalT)
                            if proceso == 1:
                                self._ZoologicoC.setTotalAZoo(-1)
                                st.success("El Animal Fue Enviado a la Bodega Con Exito.")
                                st.session_state["Zoologico"] = self._ZoologicoC
                            else:
                                st.error(proceso)
                        else:
                            st.error(animalT)
                        self.cronometro(5)

        elif eleccionH == "Interactuar Animal":
            if len(habitatI.getVectorAH()) > 0:
                idAnimal = None
                dicInversoA = {"": 0}
                habitat: list[AnimalM.Animal] = habitatI.getVectorAH()
                for animalE in habitat:
                    newValA = animalE.getIdAnimal()
                    newClaveA = animalE.getNombreAnimal()  + " - " + animalE.getNombreEspecie()
                    dicInversoA[newClaveA] = newValA

                cajaAnimalesB = st.selectbox("Elige un Animal: ", list(dicInversoA.keys()))
                idAnimal = dicInversoA[cajaAnimalesB]
                if cajaAnimalesB != 0:


                    animal = habitatI.retornarAnimal(idAnimal)
                    if type(animal) != str:
                        self._viewZoologico.mostrarAnimal(animal)
                        # Crear las pestañas
                        tabs = ["Comer", "Dormir", "Jugar"]
                        active_tab = st.sidebar.radio("Opciones", tabs)
                        if active_tab == "Comer":  # Pestaña Comer
                            #self._viewZoologico.
                            st.header("Comer")
                            alimento = st.text_input("Ingrese el Alimento")
                            if st.button("Enviar Comida", key="comer"):
                                comer = animal.Comer(self._AlimentoM, alimento)
                                self.cronometro(5)

                        if active_tab == "Dormir":  # Pestaña Dormir
                            st.header("Dormir")
                            if st.button("Enviar Dormir", key="dormir"):
                                dormir = animal.dormir()
                                self.cronometro(5)
                        if active_tab == "Jugar":  # Pestaña Jugar
                            st.header("Jugar")
                            if st.button("Enviar Juego", key="jugar"):
                                jugar = animal.jugar()
                                self.cronometro(5)
                    else:
                        st.error(animal)
                    self.cronometro(5)
            else:
                st.info("No Hay Animales en el Habitat.")

            st.session_state["Zoologico"] = self._ZoologicoC

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
                    self._ZoologicoC.modiCreadorId()
                    st.session_state["Zoologico"] = self._ZoologicoC
                    st.success("Animal Ingresado Correctamente en la Bodega")
                else:
                    st.error(resIngre)
                self.cronometro(5)
        elif eleccionB == "Eliminar Animal":
            if len(self._ZoologicoC.getBodega()) > 0:
                idAnimal = None
                dicInversoA = {"": 0}
                bodega: list[AnimalM.Animal] = self._ZoologicoC.getBodega()
                for animalE in bodega:
                    tuplaTa = animalE.getTuplaTemA()
                    newValA = animalE.getIdAnimal()
                    newClaveA = animalE.getNombreEspecie() + " - " + animalE.getTipoAdapA_str() + " - " + animalE.getTipoHabitad_str()  + " - Tem[" + str(tuplaTa[0]) + "/" + str(tuplaTa[1]) + "]"
                    dicInversoA[newClaveA] = newValA

                cajaAnimalesB = st.selectbox("Elige un Animal: ", list(dicInversoA.keys()))
                idAnimal = dicInversoA[cajaAnimalesB]
                if cajaAnimalesB != 0:
                    botonAB = st.button("Sacar de Bodega")
                    if botonAB == True:
                        resProceso = self._ZoologicoC.eliminarAnimalBodega(idAnimal)
                        if resProceso == 1:
                            st.session_state["Zoologico"] = self._ZoologicoC
                            st.success("Eliminado con Exito")
                        else:
                            st.error(resProceso)
                        self.cronometro(5)
                    else:
                        st.session_state["Zoologico"] = self._ZoologicoC
        elif eleccionB == "Mover a Habitat":
            col = st.columns(2)
            if len(self._ZoologicoC.getBodega()) > 0 and self._ZoologicoC.getTotalAZoo() > 0:
                idAnimalM = None
                keyHabitatB = None
                with col[0]:
                    dicInversoA = {"": 0 }
                    bodega : list[AnimalM.Animal] = self._ZoologicoC.getBodega()
                    for animal in bodega:
                        tuplaTa = animal.getTuplaTemA()
                        newValA = animal.getIdAnimal()
                        newClaveA = animal.getNombreEspecie() + " - " + animal.getTipoAdapA_str() + " - " + animal.getTipoHabitad_str() + " - Tem[" + str(tuplaTa[0]) + "/" + str(tuplaTa[1]) + "]"
                        dicInversoA[newClaveA] = newValA
                    cajaAnimalesBM = st.selectbox("Elige un Animal: ", list(dicInversoA.keys()))
                    idAnimalM = dicInversoA[cajaAnimalesBM]
                with col[1]:
                    dicInverso = {"": 0} # clave string "key - adecuacion - tem" y su valor sera la key "Entero"
                    mapa = self._ZoologicoC.getMapa()
                    for key in mapa:
                        temH: HabitatM.Habitat = mapa[key]
                        tuplaH = temH.getTuplaTemH()
                        newClave = str(key) + " - " + temH.getAdecuacion_Str() + " - " + temH.getTipoH_Str() + " - Tem["+ str(tuplaH[0]) + "/" + str(tuplaH[1])+"]"
                        dicInverso[newClave] = key
                    cajaHabitats = st.selectbox("Elige una Habitat: ", list(dicInverso.keys()))
                    keyHabitatB = dicInverso[cajaHabitats] # Key del habitat en el zoo
                if cajaAnimalesBM != 0:
                    botonAB = st.button("Mover")
                    if botonAB == True:
                        animalB: AnimalM.Animal = self._ZoologicoC.sacarAnimalBodega(idAnimalM)
                        if type(animalB) != str:
                            resProcesoIngreso = self._ZoologicoC.agregarAnimalH(animalB, keyHabitatB)
                            if resProcesoIngreso == 1:
                                st.success("Animal Ingresado en el Habitat con el Id " +str(keyHabitatB) + ".")
                                st.success("Correctamente.")
                                st.session_state["Zoologico"] = self._ZoologicoC
                            else:
                                st.session_state["Zoologico"] = self._ZoologicoC
                                st.error(resProcesoIngreso)
                        else:
                            st.session_state["Zoologico"] = self._ZoologicoC
                            st.error(animalB)
                        self.cronometro(5)
                    else:
                        st.session_state["Zoologico"] = self._ZoologicoC
            else:
                st.info("No Hay Animales en el Zoologico")
        elif eleccionB == "Mostrar Bodega":
            bodega = self._ZoologicoC.getBodega()
            self._viewZoologico.mostrarBodega(bodega)
        st.session_state["Zoologico"] = self._ZoologicoC
    def menuZoo(self):

        # Mantén el programa en ejecución para continuar capturando clics
        st.markdown(f"<h1 style='text-align: center; color: green;font-family: Times New Roman;margin-top: -50px;background-color: #d9f2c3;'>{self._ZoologicoC.getNombre()}</h1>", unsafe_allow_html=True)
        menu = ["Ver Mapa Zoologico", "Crear Habitat", "Ver Habitat", "Eliminar Habitat del Zoologico", "Bodega", "Alimentos","Biblioteca"]
        eleccionMenu = st.sidebar.selectbox("Seleccione una opción", menu)
        if eleccionMenu == "Ver Mapa Zoologico":
            mapa = self._ZoologicoC.getMapa()
            totalA = self._ZoologicoC.getTotalAZoo()
            totalH = self._ZoologicoC.getTotalHZoo()
            self._viewZoologico.mostrarHabitats(mapa,totalA,totalH)
        elif eleccionMenu == "Crear Habitat":
            tuplaT = None
            columnas = st.columns(3)
            listaInfo = self._viewZoologico.paneles(columnas)
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
                    self.cronometro(5)

        elif eleccionMenu == "Ver Habitat":
            dicInverso = {"": 0}
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
                if 0 != eleccion:
                    st.write(eleccion)
                    self.submenuHabitat(self._ZoologicoC.getMapa()[eleccion], eleccion)


        elif eleccionMenu == "Eliminar Habitat del Zoologico":
            if self._ZoologicoC.getTotalHZoo() > 0:
                dicInverso = {"" : 0}
                mapa = self._ZoologicoC.getMapa()
                for key in mapa:
                    temH:HabitatM.Habitat = mapa[key]
                    newClave = str(key) + " - " + temH.getAdecuacion_Str()+ " - Total Animales: "+str(temH.getCantidadAH()) +" - "+ temH.getTipoH_Str()
                    dicInverso[newClave] = key
                cajaHabitats = st.selectbox("Elige un habitat", list(dicInverso.keys()))
                eleccion = dicInverso[cajaHabitats]
                if eleccion != 0:
                    botonE = st.button("ELIMINAR")
                    if botonE == True:
                        resProceso = self._ZoologicoC.eliminarHabitat(eleccion)
                        st.write(resProceso)
                        if resProceso == 1:
                            st.session_state["Zoologico"] = self._ZoologicoC
                            st.success("El Habitat seleccionado fue eliminado Correctamente.")
                        else:
                            st.error(resProceso)
                        self.cronometro(5)
            else:
                st.info("NO HAY HABITATS EN EL ZOOLOGICO")
        elif eleccionMenu == "Bodega":
            self.subMenuBodega()

        elif eleccionMenu == "Alimentos":
            options = ["","Agregar Alimento", "Sacar Alimento", "Ver Alimentos","Editar Alimento"]
            sub_selection = st.sidebar.selectbox("Seleccione una subopción", options)
            st.sidebar.subheader(f"Subopción seleccionada: {sub_selection}")
 
            if sub_selection == "Agregar Alimento":
        
                data = self._viewZoologico.menuAgregarAlimento()
                if data:
                    if data[1] == "Herviboro":
                        if self._AlimentoM.addHerbivoros(data[2],data[0]):
                            st.success("Alimento Guardado")
                        else:
                            st.success("No se guardo el alimento")
                        self.cronometro(5)
                    elif data[1] == "Carnivoro":
                        if self._AlimentoM.addCarnivoros(data[2],data[0]):
                            st.success("Alimento Guardado")
                        else:
                            st.success("No se guardo el alimento")
                        self.cronometro(5)
                    st.session_state["comida"] = self._AlimentoM

                    
            elif sub_selection == "Sacar Alimento":
            
                alimentos_seleccionados = self._viewZoologico.mostrarSeleccionDelete(self._AlimentoM)
                
                if len(alimentos_seleccionados) > 0:
                    if st.button("Sacar Alimentos"):
                        for categoria in self._AlimentoM.categorias:
                            categoria[:] = [alimento for alimento in categoria if alimento not in alimentos_seleccionados]
                        st.success("Alimentos Sacados")
                        st.session_state["comida"] = self._AlimentoM
                        self.cronometro(5)
                else:
                    st.write("No hay alimentos")
        
            elif sub_selection == "Ver Alimentos":
                self._viewZoologico.mostrarAlimentos(self._AlimentoM)

            elif sub_selection == "Editar Alimento":
                try:
                    alimento_seleccionado, alimento_reemplazo = self._viewZoologico.mostrarSeleccionEdit(self._AlimentoM)
                except Exception as e:
                    alimentos_seleccionados = None
                    alimento_reemplazo = None
                if alimento_reemplazo is not None:
                    if alimento_seleccionado is not None:
                        for categoria in self._AlimentoM.categorias:
                            if alimento_seleccionado in categoria:
                                
                                index = categoria.index(alimento_seleccionado)
                                categoria[index] = alimento_reemplazo
                                st.session_state["comida"] = self._AlimentoM
                                st.success("Alimento Editado")
                                break
                            else:
                                pass
                            self.cronometro(5)
                    else:
                        st.success("No se seleccionó ningún alimento para reemplazar")
        elif eleccionMenu == "Biblioteca":

                habitats = {1: "Selvático", 2: "Bosque", 3: "Desértico", 4: "Oceánico", 5: "Polar", 6: "Manglar", 7: "Snow Leopard", 8: "Tropical", 9: "Sabana"}           
            
                animal_names = {1: "Bengal Tiger",2: "Red Fox",3: "Rattlesnake",
                                4: "Dolphin",5: "Polar Bear",6: "Mangrove Snake",
                                7: "Snow Leopard",8: "Toucan",9: "Lion"
                            }
                media = os.path.join(os.path.dirname(__file__), "../media")
                animal_images = {
                        "Bengal Tiger": os.path.join(media, "Bengal Tiger.jpg"),
                        "Red Fox": os.path.join(media, "Red Fox.jpg"),
                        "Rattlesnake": os.path.join(media, "Rattlesnake.jpg"),
                        "Dolphin": os.path.join(media, "Dolphin.jpg"),
                        "Polar Bear": os.path.join(media, "Polar Bear.jpg"),
                        "Mangrove Snake": os.path.join(media, "Mangrove Snake.jpeg"),
                        "Snow Leopard": os.path.join(media, "Snow Leopard.jpg"),
                        "Toucan": os.path.join(media, "Toucan.jpg"),
                        "Lion": os.path.join(media, "Lion.jpg")         
                }
                selected_habitat = st.sidebar.selectbox("Selecciona un hábitat", list(habitats.values()))
                st.subheader(f"Hábitat: {selected_habitat}")
                animal_name = animal_names.get(list(habitats.keys())[list(habitats.values()).index(selected_habitat)])
                
                if animal_name:
                    api_url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
                    headers = {'X-Api-Key': 'NIuMGUWYpQXt/6xruXcq9Q==wWYp8Q98OfKUWLpm'}

                    try:
                        response = requests.get(api_url, headers=headers)
                        response.raise_for_status()
                        animal_info = response.json()[0]

                        st.write("Nombre:", animal_info['name'])

                        image_url = animal_images.get(animal_name)
                        if image_url:
                            st.image(image_url, caption=f"Imagen de {animal_info['name']}", use_column_width=True)
                        else:
                            st.warning("No se encontró la imagen del animal")

                        st.write("Hábitat:", selected_habitat)
                        st.write("Clasificación:", animal_info['taxonomy'].get('class', 'No disponible'))
                        st.write("Dieta:", animal_info['characteristics'].get('diet', 'No disponible'))
                        st.write("Velocidad Máxima:", animal_info['characteristics'].get('top_speed', 'No disponible'))
                        st.write("Esperanza de Vida:", animal_info['characteristics'].get('lifespan', 'No disponible'))
                        st.write("Peso:", animal_info['characteristics'].get('weight', 'No disponible'))
                        st.write("Longitud:", animal_info['characteristics'].get('length', 'No disponible'))
                    except (requests.exceptions.RequestException, IndexError) as e:
                        st.error(f"Error en la llamada a la API para el hábitat {selected_habitat}: {e}")
                else:
                    st.warning("No se encontró un animal para este hábitat")

        st.session_state["Zoologico"] = self._ZoologicoC

    



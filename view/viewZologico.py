
import model.Zoologico
import model.Habitat
import model.Animal
import streamlit as st

class viewZoologico:
    def __init__(self):
        self.dicDieta = {1:"Carnivora" , 2:"Herbibora", 3: "Omnivora"}

    def mostrarHabitats(self,mapa:dict[int,model.Habitat.Habitat],totalA:int,totalH:int):
        if totalH > 0:
            st.title("El Zoologico Cuenta con " + str(totalH) +" Habitats actualmente.")
            st.title("El Zoologico cuenta con "+ str(totalA) + " Animales actualmente.\n")
            for key in mapa:
                st.write(" ----- Habitat con el Id: " + str(key))
                st.write(" ------- Tipo de Habitat: " + str(mapa[key].getTipoH_Str()))
                st.write(" ------- Tipo de Adecuacion: " + str(mapa[key].getAdecuacion_Str()))
                st.write(" ------- Dieta de los Animales: " + str(self.dicDieta[mapa[key].getTipoDieta()]))
                st.write(" ------- Cantidad Animales dentro del Habitat: "+ str(mapa[key].getCantidadAH()))
                st.write(" ------- Tem Min = "+ str(mapa[key].getTuplaTemH()[0])+" - Tem Max = "+str(mapa[key].getTuplaTemH()[1])+ " Cº")
        else:
            st.markdown("<h1 style='text-align: center;'>Alerta</h1>", unsafe_allow_html=True)
            st.warning("El Zoologico se encuentra vacio no hay habitats aun.")

    def mostrarAnimal( self,animal : model.Animal ):
        columnas = st.columns(2)
        with columnas[0]:
            st.write("   El animal con el id: " + str(animal.getIdAnimal()))
            st.write("      _[*] Especie: "+ animal.getNombreEspecie())
            st.write("      _[*] Nombre: "+ animal.getNombreAnimal())
            st.write("      _[*] Edad: "+ str(animal.getedad()))
            st.write("      _[*] Tipo Adaptacion: "+ animal.getTipoAdapA_str())
        with columnas[1]:
            st.write("")
            st.write("")
            st.write("")
            st.write("      [*] Tipo Habitat: "+ animal.getTipoHabitad_str())
            st.write("      [*] Tipo de Dieta: "+ self.dicDieta[animal.getTipoDieta()])
            st.write("      [*] Temperatura Min: "+ str(animal.getTuplaTemA()[0])+ " Cº")
            st.write("      [*] Temperatura Max: "+ str(animal.getTuplaTemA()[1])+ " Cº")

    def mostrarAnimalesHabitat(self,habitatH : model.Habitat.Habitat,  keyH:int):
        if habitatH.getCantidadAH() > 0 :
            st.write("En este Habitat con el clave "+ str(keyH)+ ", con una adecuacion de tipo "+ habitatH.getAdecuacion_Str()+ " y una dieta "+ self.dicDieta[habitatH.getTipoDieta()])
            st.write("Que posee una temperatura entre los "+str(habitatH.getTuplaTemH()[0])+" - "+str(habitatH.getTuplaTemH()[1])+ " Cº")
            vectorH = habitatH.getVectorAH()
            i = 0
            while i < len(vectorH):
                self.mostrarAnimal(vectorH[i])
                i+=1
        else:
            st.markdown("<h1 style='text-align: center;'>Alerta</h1>", unsafe_allow_html=True)
            st.warning("No Hay Animales en Habitat.")
    def paneles(self, columnas):
        with columnas[0]:
            optionsA = {"Terrestre": 1,"Acuatico": 2,"SemiAcuatico": 3,"Volador":4}
            panel1 = st.radio("Selecciona el tipo de Adecuacion:", list(optionsA.keys()))
            optionsD = {"Carnivoro": 1, "Herbivoro": 2, "Omnivoro": 3}
            panel2 = st.radio("Selecciona el tipo de Dieta", list(optionsD.keys()))
        with columnas[1]:
            optionsH = {"Selvatico":1,"Bosque":2,"Desertico":3,"Ocenico":4,
                    "Polar":5,"Manglar":6,"Montañoso":7,"Tropical":8,"Sabana":9}
            panel3 = st.radio("Selecciona el Tipo de Habitat: ", list(optionsH.keys()))
        return [optionsA[panel1],optionsD[panel2],optionsH[panel3]]

    def mostrarBodega(self,bodega:list[model.Animal.Animal]):
        tamB = len(bodega)
        if tamB == 0:
            st.write("! Bodega Vacia ¡")
            st.info("No hay Animales dentro de la bodega")
        else:
            st.title("Animales en Bodega = "+ str(tamB))
            for animal in bodega:
                self.mostrarAnimal(animal)
    
    def menuAgregarAlimento(self):
        st.title("Agregar Alimentos")
        habitat_selection = st.radio("Tipo de Hábitat", ["Terrestres", "Acuaticos", "Subacuaticos", "Voladores"])
        alimentacion_selection = st.radio("Tipo de Alimentación", ["Herbivoro", "Carnivoro"])
        alimento_input = st.text_input("Alimento")
        guardar_button = st.button("Guardar")

        if habitat_selection == "Terrestres": habitat_selection = 1
        elif habitat_selection == "Acuaticos": habitat_selection = 2
        elif habitat_selection == "Subacuaticos": habitat_selection = 3
        else: habitat_selection = 4

        if guardar_button:
            alimento = [habitat_selection, alimentacion_selection, alimento_input]
            return alimento
        else:
            return []

    def mostrarAlimentos(self, Alimentos):
        categorias = ["Terrestres", "Acuáticos", "SemiAcuáticos", "Voladores"]
        tipos_alimentos = ["Carnívoros", "Herbívoros"]

        categoria_seleccionada = st.radio("Seleccione una categoría:", categorias)
        tipo_alimento_seleccionado = st.radio("Seleccione el tipo de alimento:", tipos_alimentos)

        if categoria_seleccionada == "Terrestres":
            alimentos = Alimentos.terrestresC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.terrestresH
        elif categoria_seleccionada == "Acuáticos":
            alimentos = Alimentos.acuaticoC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.acuaticoH
        elif categoria_seleccionada == "SemiAcuáticos":
            alimentos = Alimentos.semiAcuaticoC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.semiAcuaticoH
        elif categoria_seleccionada == "Voladores":
            alimentos = Alimentos.voladorC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.voladorH

        for alimento in alimentos:
            if len(alimentos) > 0:
                st.write(alimento)
            else: st.write("No hay alimentos")

    def mostrarSeleccionDelete(self, Alimentos):
        alimentos_seleccionados = []

        categorias = ["Terrestres", "Acuáticos", "SemiAcuáticos", "Voladores"]
        tipos_alimentos = ["Carnívoros", "Herbívoros"]

        categoria_seleccionada = st.radio("Seleccione una categoría:", categorias)
        tipo_alimento_seleccionado = st.radio("Seleccione el tipo de alimento:", tipos_alimentos)

        if categoria_seleccionada == "Terrestres":
            alimentos = Alimentos.terrestresC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.terrestresH
        elif categoria_seleccionada == "Acuáticos":
            alimentos = Alimentos.acuaticoC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.acuaticoH
        elif categoria_seleccionada == "SemiAcuáticos":
            alimentos = Alimentos.semiAcuaticoC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.semiAcuaticoH
        elif categoria_seleccionada == "Voladores":
            alimentos = Alimentos.voladorC if tipo_alimento_seleccionado == "Carnívoros" else Alimentos.voladorH

        for alimento in alimentos:
            seleccionado = st.radio("", alimentos)
            if seleccionado:
                alimentos_seleccionados.append(seleccionado)

        return alimentos_seleccionados


    def mostrarSeleccionEdit(self, Alimentos):
        categorias = ["Terrestres", "Acuáticos", "SemiAcuáticos", "Voladores"]
        tipos_alimentos = ["Carnívoros", "Herbívoros"]
        alimentos_seleccionados = []
        contador = 0

        seleccion_categoria = st.radio("Seleccione una categoría:", categorias)
        seleccion_tipo = st.radio("Seleccione un tipo de alimento:", tipos_alimentos)

        if seleccion_categoria and seleccion_tipo:
            if seleccion_categoria == "Terrestres" and seleccion_tipo == "Carnívoros":
                alimentos = Alimentos.terrestresC
            elif seleccion_categoria == "Terrestres" and seleccion_tipo == "Herbívoros":
                alimentos = Alimentos.terrestresH
            elif seleccion_categoria == "Acuáticos" and seleccion_tipo == "Carnívoros":
                alimentos = Alimentos.acuaticoC
            elif seleccion_categoria == "Acuáticos" and seleccion_tipo == "Herbívoros":
                alimentos = Alimentos.acuaticoH
            elif seleccion_categoria == "SemiAcuáticos" and seleccion_tipo == "Carnívoros":
                alimentos = Alimentos.semiAcuaticoC
            elif seleccion_categoria == "SemiAcuáticos" and seleccion_tipo == "Herbívoros":
                alimentos = Alimentos.semiAcuaticoH
            elif seleccion_categoria == "Voladores" and seleccion_tipo == "Carnívoros":
                alimentos = Alimentos.voladorC
            elif seleccion_categoria == "Voladores" and seleccion_tipo == "Herbívoros":
                alimentos = Alimentos.voladorH

            st.subheader("Seleccione un elemento:")
            seleccionado = st.selectbox("Elemento seleccionado", ["Ninguno"] + alimentos)

            if seleccionado != "Ninguno":
                alimentos_seleccionados.append(seleccionado)

            alimento_reemplazo = st.text_input("Ingrese el alimento de reemplazo")
            if st.button("Remplazar"):
                alimento_seleccionado = alimentos_seleccionados[0] if alimentos_seleccionados else None
                if alimento_seleccionado is not None and alimento_reemplazo is not None:
                    return alimento_seleccionado, alimento_reemplazo

    

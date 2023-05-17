
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


    def menuInteracciones(self,animalh:model.Animal):
        Animal = animalh
        print("|   El se llama  ",Animal.getNombreAnimal()," es de la espcie ",Animal.getNombreEspecie())
        print("  Tiene ", Animal.getedad(), " Años y es ",self.dicDieta[Animal.getTipoDieta()])
        print("Que accion quieres hacer con el ?")
        print("[1] Comer")
        print("[2] Jugar")
        print("[3] Dormir")
        print("[0] Salir  \n")
        print("Ingrese la obcion deseada: ")
    def mostrarBodega(self,bodega:list[model.Animal.Animal]):
        tamB = len(bodega)
        if tamB == 0:
            st.write("! Bodega Vacia ¡")
            st.info("No hay Animales dentro de la bodega")
        else:
            st.title("Animales en Bodega = "+ str(tamB))
            for animal in bodega:
                self.mostrarAnimal(animal)

    def menuAlimentos(self):

        print("[1] Terrestres")
        print("[2] Acuaticos")
        print("[3] Semi Acuaticos")
        print("[4] Voladores")
        print("[0] Salir")
        print("[*] Ingrese la opcion deseada: ")

    def subMenuAlimentos(self):
        
        print("[1] Carnivoros")
        print("[2] Herbivoros")
        print("[3] Omnivoros")
        print("[*] Ingrese la opcion deseada: ")
    """
    def printAlimentos(self, ocpT, ocpD,alimento):

        if ocpT == 1 and ocpD == 1:
            for i in alimento.terrestresC: print(i)

        elif ocpT == 1 and ocpD == 2:
            for i in alimento.terrestresH: print(i)

        elif ocpT == 1 and ocpD == 3:
            for i, j in zip(alimento.terrestresC, alimento.terrestresH):
                print(f"{terrestresC:<10} {terrestresH}")
        
        elif ocpT == 2 and ocpD == 1:
            for i in alimento.acuaticoC: print(i)

        elif ocpT == 2 and ocpD == 2:
            for i in alimento.acuaticoH: print(i)
        
        elif ocpT == 2 and ocpD == 3:
             for i, j in zip(alimento.acuaticoC, alimento.acuaticoH):
                print(f"{acuaticoC:<10} {acuaticoH}")

        elif ocpT == 3 and ocpD == 1:
            for i in alimento.semiAcuaticoC: print(i)

        elif ocpT == 3 and ocpD == 2:
            for i in alimento.semiAcuaticoH: print(i)
        
        elif ocpT == 3 and ocpD == 3:
             for i, j in zip(alimento.semiAcuaticoC, alimento.semiAcuaticoH):
                print(f"{semiAcuaticoC:<10} {semiAcuaticoH}")

        elif ocpT == 4 and ocpD == 1:
            for i in alimento.voladorC: print(i)

        elif ocpT == 4 and ocpD == 2:
            for i in alimento.voladorH: print(i)

        elif ocpT == 4 and ocpD == 3:
             for i, j in zip(alimento.voladorC, alimento.voladorH):
                print(f"{voladorC:<10} {voladorH}")
    """






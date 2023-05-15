
import model.Zoologico
import model.Habitat
import model.Animal
import streamlit as st

class viewZoologico:
    def __init__(self):
        self.dicDieta = {1:"Carnivora" , 2:"Herbibora", 3: "Omnivora"}
    def menuZoologico(self, zoologicoA:model.Zoologico):

        print("*** | Bienvenido al Zoologico ", zoologicoA.getNombre," | **\n")
        print("[1] Ver mapa Zoologico ")
        print("[2] Crear habitat ")
        print("[3] Ver Habitat ")
        print("[4] Eliminar Habitad del Zoologico.")
        print("[5] Bodega")
        print("[0] Salir del Zoologico \n")
        print ("Ingrese la obcion deseada: ")



    def mostrarHabitats(self,mapa:dict,totalA:int,totalH:int):
        if totalH > 0:
            st.write("El Zoologico Cuenta con " + str(totalH) +" Habitats actualmente.")
            st.write("El Zoologico cuenta con"+ str(totalA) + " Animales actualmente.\n")
            for key, Habitat in mapa:
                st.write("  Habitat con el Id: " + str(key))
                st.write("      Tipo de Habitat: " + str(Habitat.getTipoH_Str()))
                st.write("      Tipo de Adecuacion: " + str(Habitat.getAdecuacion_Str()))
                st.write("      Dieta de los Animales: " + self.dicDieta[Habitat.getTipoDieta()])
                st.write("      Cantidad Animales dentro del Habitat: "+ str(Habitat.getCantidadAH()))
                st.write("      Tem Min = "+ str(Habitat.getTuplaTemH()[0])+" - Tem Max = "+str(Habitat.getTuplaTemH()[1])+ " Cº")
        else:
            st.markdown("<h1 style='text-align: center;'>Alerta</h1>", unsafe_allow_html=True)
            st.warning("El Zoologico se encuentra vacio no hay habitats aun.")

    def mostrarAnimal( self,animal : model.Animal ):

        st.write("    El animal con el id: "+ str(animal.getIdAnimal()))
        st.write("      [*] Especie: "+ animal.getNombreEspecie())
        st.write("      [*] Nombre: "+ animal.getNombreAnimal())
        st.write("      [*] Edad: "+ str(animal.getedad()))
        st.write("      [*] Tipo Adaptacion: "+ animal.getTipoAdapA_str())
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
            optionsA = {"Terrestres": 1,"Acuaticos ": 2,"SemiAcuaticos": 3,"Volador":4}
            panel1 = st.radio("Selecciona una opción", list(optionsA.keys()))
            optionsD = {"Carnivoro": 1, "Herbivoro": 2, "Omnivoro": 3}
            panel2 = st.radio("Selecciona una opción", list(optionsD.keys()))
        with columnas[1]:
            optionsH = {"Selvatico":1,"Bosque":2,"Desertico":3,"Ocenico":4,
                    "Polar":5,"Manglar":6,"Montañoso":7,"Tropical":8,"Sabana":9}
            panel3 = st.radio("Selecciona una opción", list(optionsH.keys()))
        return [optionsA[panel1],optionsD[panel2],optionsH[panel3]]

    def subMenuHabitat(self,habitat:model.Habitat,idH:int):
        print("*** |  Bienvenido al Habitat ",idH ," ", habitat.getTipoH_Str()," | ***")
        print("** |   Adecuado para especies de tipo ",habitat.getAdecuacion_Str())
        print("[1] Agregar Animal al habitat")
        print("[2] Sacar Animal del Zoologico")
        print("[3] Mostrar Animales dentro del habitat ")
        print("[4] Interactuar Animal ")
        print("[0] Salir del habitat \n")
        print("Ingrese la obcion deseada: ")


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
    def mostrarTituloMenuP(self,opcS:int):
        res = ""
        if opcS == 1:
            res = "[--] Mapa Zoologico [--]"
        elif opcS == 2:
            res = "[--] Creando Habitat [--]"
        elif opcS == 3:
            res = "[--] Dirigiendose al Habitat[--]"
        elif opcS == 4:
            res = "[--] Eliminar Habitat del Zoologico [--]"
        elif opcS == 5:
            res = "[--] Bodega del Zoologico [--]"
        elif opcS == 0:
            res = "[--] Saliendo [--]"
        else:
            res = "OPCION INVALIDA INTENTELO NUEVAMENTE"
        print(res)
    def mostrarTitulosSubMenuH(self,opcH:int):
        if opcH == 1:
            res = "[--] Agregar Animal Habitat [--]"
        elif opcH == 2:
            res = "[--] Sacar Animal Zoologico [--]"
        elif opcH == 3:
            res = "[--] Cargando Animales [--]"
        elif opcH == 4:
            res = "[--] Hacercandose al Animal  [--]"
        elif opcH == 0:
            res = "[--] Saliendo del Habitat [--]"
        else:
            res = "OPCION INVALIDA INTENTELO NUEVAMENTE"

    def menuBodega(self):
        print("*** |  Bienvenido ala Bodega del Zoologico | ***")
        print("[1] Agregar Animal")
        print("[2] Eliminar Animal ")
        print("[3] Mover a Habitat")
        print("[4] Mostrar Bodega ")
        print("[0] Salir de la bodega \n")
        print("Ingrese la obcion deseada: ")

    def mostrarTitulosSubMenuB(self,opcH:int):
        if opcH == 1:
            res = "[--] Agregar Animal a la bodega [--]"
        elif opcH == 2:
            res = "[--] Sacar Animal de la bodega[--]"
        elif opcH == 3:
            res = "[--] Trasladar Animal [--]"
        elif opcH == 4:
            res = "[--] Mostrando Bodega [--]"
        elif opcH == 0:
            res = "[--] Saliendo del la bodega[--]"
        else:
            res = "OPCION INVALIDA INTENTELO NUEVAMENTE"

    def mostrarBodega(self,bodega:list[model.Animal]):
        tamB = len(bodega)
        if tamB == 0:
            print("! Bodega Vacia ¡")
            print("No hay Animales dentro de la bodega")
        else:
            print("Animales en Bodega = ",tamB)
            i = 0
            while i < tamB:
                self.mostrarAnimal(bodega[i])

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






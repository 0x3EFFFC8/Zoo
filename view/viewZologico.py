
import model.Zoologico
import model.Habitat
import model.Animal

class viewZoologico:
    def __init__(self):
        self.dicDieta = {1:"Carnivora" , 2:"Herbibora", 3: "Omnivora"}
    def menuZoologico(self, zoologicoA:model.Zoologico):

        print("*** | Bienvenido al Zoologico ", zoologicoA.getNombre," | **\n")
        print("[1] Ver mapa Zoologico ")
        print("[2] Crear habitat ")
        print("[3] Ver Habitat ")
        print("[4] Eliminar Habitad del Zoologico ")
        print("[5] Mover Animal de Habitat")
        print("[6] Bodega")
        print("[0] Salir del Zoologico \n")
        print ("Ingrese la obcion deseada: ")



    def mostrarHabitats(self,zoologicoA : model.Zoologico):
        mapa = zoologicoA.getMapa
        if len(mapa) != 0:
            print("El Zoologico Cuenta con ", zoologicoA.getTotalHZoo(), " Habitats actualmente.")
            print("El Zoologico cuenta con", zoologicoA.getTotalAZoo(), " Animales actualmente.\n")
            for key, Habitat in mapa:
                print("  Habitat con el Id: ", key)
                print("      Tipo de Habitat: ", Habitat.getTipoH_Str())
                print("      Tipo de Adecuacion: ", Habitat.getAdecuacion_Str())
                print("      Dieta de los Animales: ", self.dicDieta[Habitat.getTipoDieta()])
                print("      Cantidad Animales dentro del Habitat: ", Habitat.getCantidadAH())
                print("      Tem Min = ", Habitat.getTuplaTemH()[0]," - Tem Max = ",Habitat.getTuplaTemH()[1], " Cº")
        else:
            print("El Zoologico se encuentra vacio no hay habitats aun.")

    def mostrarAnimal( self,animal : model.Animal ):

        print("    El animal con el id: ", animal.getIdAnimal())
        print("      [*] Especie: ", animal.getNombreEspecie())
        print("      [*] Nombre: ", animal.getNombreAnimal())
        print("      [*] Edad: ", animal.getedad())
        print("      [*] Tipo Adaptacion: ", animal.getTipoAdapA_str())
        print("      [*] Tipo Habitat: ", animal.getTipoHabitad_str())
        print("      [*] Tipo de Dieta: ", self.dicDieta[animal.getTipoDieta()])
        print("      [*] Temperatura Min: ", animal.getTuplaTemA()[0], " Cº")
        print("      [*] Temperatura Max: ", animal.getTuplaTemA()[1], " Cº")

    def mostrarAnimalesHabitat(self,habitatH : model.Habitat,  keyH:int):
        Habitat = habitatH
        print("En este Habitat con el clave ", keyH, ", con una adecuacion de tipo ", Habitat.getAdecuacion_Str(), " y una dieta ", self.dicDieta[Habitat.getTipoDieta()] )
        print("Que posee una temperatura entre los ",Habitat.getTuplaTemH()[0]," - ",Habitat.getTuplaTemH()[1], " Cº")
        vectorH = habitatH.getVectorAH()
        i = 0
        while i < len(vectorH):
            self.mostrarAnimal(vectorH[i])
            i+=1

    def panelAdecuacion(self):

        print("[1] Terrestres")
        print("[2] Acuaticos")
        print("[3] SemiAcuatico")
        print("[4] Volador")
        print("Elija una de esas opciones: ")

    def panelDieta(self):
        print("[1] Carnivoro")
        print("[2] Herbiboro")
        print("[3] Omniboro")
        print("Elija una de esas opciones: ")

    def panelTipoHabitat(self):
        print("[1] Selvatico")
        print("[2] Bosque")
        print("[3] Desertico")
        print("[4] Oceanico")
        print("[5] Polar")
        print("[6] Manglar")
        print("[7] Montañoso")
        print("[8] Tropical")
        print("[9] Sabana")
        print("Elija una de esas opciones: ")

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
            res = "[--] Mover Animal de Habitat [--]"
        elif opcS == 6:
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






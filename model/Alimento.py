class Alimento:
    def __init__(self):
        self.carnivoros = set()
        self.herbivoros = set()
    
    def addCarnivoros(self, alimento):
        self.carnivoros.add(alimento)
    
    def addHerbivoros(self, alimento):
        self.herbivoros.add(alimento)
    
    def verificarCarnivoros(self, alimento):
        return alimento in self.carnivoros
    
    def verificarHerbivoros(self, nombre):
        return alimento in self.herbivoros

    def imprimirAlimentos(self):
        print("Carnivoros\tHerbivoros")
        print("----------\t----------")
        for i, j in zip(self.carnivoros, self.herbivoros):
            print(f"{i}\t\t{j}")

    def editAlimento(self, alimento_old, alimento_new, tipo_animal):
        if tipo_animal == 1:
            if alimento_old in self.carnivoros:
                self.carnivoros.discard(alimento_old)
                self.carnivoros.add(alimento_new)
            else:
                print("El alimento no se encuentra en la lista de alimentos para carnívoros.")
        elif tipo_animal == 2:
            if alimento_old in self.herbivoros:
                self.herbivoros.discard(alimento_old)
                self.herbivoros.add(alimento_new)
            else:
                print("El alimento no se encuentra en la lista de alimentos para herbívoros.")
        else
            if alimento_old in self.carnivoros:
                self.carnivoros.discard(alimento_old)
                self,carnivoros.add(alimento_new)
            else if alimento_old in self.herbivoros:
                self.herbivoros.discard(alimento_old)
                self.herbívoros.add(alimento_new)
            else:
                printf("El alimento no se encuentra en la lista de alimentos para omnivoro")




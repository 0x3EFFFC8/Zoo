class Alimento:
    def __init__(self):

        self.terrestresC = set()
        self.terrestresH = set()
        self.acuaticoC = set()
        self.acuaticoH = set()
        self.semiAcuaticoC = set()
        self.semiAcuaticoH = set()
        self.voladorC = set()
        self.voladorH = set()
    
    def addCarnivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresC.add(alimento)
        elif tipoAnimal == 2:
            self.acuaticoC.add(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoC.add(alimento)
        elif tipoAnimal == 4:
            self.voladorC.add(alimento)
    
    def addHerbivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresH.add(alimento)
        elif tipoAnimal == 2:
            self.acuaticoH.add(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoH.add(alimento)
        elif tipoAnimal == 4:
            self.voladorH.add(alimento)
    
    def verificarCarnivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            return alimento in self.terrestresC
        elif tipoAnimal == 2:
            return alimento in self.acuaticoC
        elif tipoAnimal == 3:
            return alimento in self.semiAcuaticoC
        elif tipoAnimal == 4:
            return alimento in self.voladorC
    
    def verificarHerbivoros(self, nombre, tipoAnimal):
        if tipoAnimal == 1:
            return alimento in self.terrestresH
        elif tipoAnimal == 2:
            return alimento in self.acuaticoH
        elif tipoAnimal == 3:
            return alimento in self.semiAcuaticoH
        elif tipoAnimal == 4:
            return alimento in self.voladorH

    def deleteAlimentoC(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresC.discard(alimento)
        elif tipoAnimal == 2:
            self.acuaticoC.discard(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoC.discard(alimento)
        elif tipoAnimal == 4:
            self.voladorC.discard(alimento)
    
    def deleteAlimentoH(self,alimento,tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresH.discard(alimento)
        elif tipoAnimal == 2:
            self.acuaticoH.discard(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoH.discard(alimento)
        elif tipoAnimal == 4:
            self.voladorH.discard(alimento)

    def editAlimentoC(self, alimento_old, alimento_new, tipo_animal, tipoDieta):
        if tipoDieta == 1:

            if tipo_animal == 1:

                if alimento_old in self.terrestresC:
                    self.terrestresC.discard(alimento_old)
                    self.terrestresC.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para carnívoros.")
            if tipo_animal == 2:

                if alimento_old in self.terrestresC:
                    self.auaticoC.discard(alimento_old)
                    self.acuaticoC.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para carnívoros.")
            if tipo_animal == 3:

                if alimento_old in self.terrestresC:
                    self.semiAcuaticoC.discard(alimento_old)
                    self.semiAcuaticoC.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para carnívoros.")
        
            if tipo_animal == 4:

                if alimento_old in self.terrestresC:
                    self.voladorC.discard(alimento_old)
                    self.voladorC.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para carnívoros.")

        elif tipoDieta == 2:
            
            if tipo_animal == 1:

                if alimento_old in self.terrestresC:
                    self.terrestresH.discard(alimento_old)
                    self.terrestresH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para herbívoros.")
            if tipo_animal == 2:

                if alimento_old in self.terrestresC:
                    self.auaticoH.discard(alimento_old)
                    self.acuaticoH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para herbívoros.")
            if tipo_animal == 3:

                if alimento_old in self.terrestresC:
                    self.semiAcuaticoH.discard(alimento_old)
                    self.semiAcuaticoH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para herbivoros.")
        
            if tipo_animal == 4:

                if alimento_old in self.terrestresC:
                    self.voladorH.discard(alimento_old)
                    self.voladorH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos para herbivoros.")

        else 
            if tipo_animal == 1:

                if alimento_old in self.terrestresC:
                    self.terrestresC.discard(alimento_old)
                    self.terrestresC.add(alimento_new)

                elif  if alimento_old in self.terrestresH:
                    self.terrestresH.discard(alimento_old)
                    self.terrestresH.add(alimento_new)

                else:
                    print("El alimento no se encuentra en la lista de alimentos.")
            if tipo_animal == 2:

                if alimento_old in self.acuaticoC:
                    self.acuaticoC.discard(alimento_old)
                    self.acuaticoC.add(alimento_new)

                elif alimento_old in self.acuaticoH:
                    self.acuaticoH.discard(alimento_old)
                    self.acuaticoH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos.")
            if tipo_animal == 3:

                if alimento_old in self.semiAcuaticoC:
                    self.semiAcuaticoC.discard(alimento_old)
                    self.semiAcuaticoC.add(alimento_new)
                
                elif alimento_old in self.semiAcuaticoH:
                    self.semiAcuaticoH.discard(alimento_old)
                    self.semiAcuaticoH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos.")
        
            if tipo_animal == 4:

                if alimento_old in self.voladorC:
                    self.voladorC.discard(alimento_old)
                    self.voladorC.add(alimento_new)

                 if alimento_old in self.voladorH:
                    self.voladorH.discard(alimento_old)
                    self.voladorH.add(alimento_new)
                else:
                    print("El alimento no se encuentra en la lista de alimentos.")






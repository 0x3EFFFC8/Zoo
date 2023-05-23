
class Alimento:
    def __init__(self):
        self.terrestresC = ["pollo crudo"]
        self.terrestresH = ["lechuga"]
        self.acuaticoC = ["sardinas"]
        self.acuaticoH = ["plangton"]
        self.semiAcuaticoC = ["ratones"]
        self.semiAcuaticoH = ["zanahoria"]
        self.voladorC = ["pollo crudo"]
        self.voladorH = ["semillas de girasol"]
        self.categorias = [
            self.terrestresC, self.terrestresH,
            self.acuaticoC, self.acuaticoH,
            self.semiAcuaticoC, self.semiAcuaticoH,
            self.voladorC, self.voladorH
        ]

    def addCarnivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresC.append(alimento)
        elif tipoAnimal == 2:
            self.acuaticoC.append(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoC.append(alimento)
        elif tipoAnimal == 4:
            self.voladorC.append(alimento)
    
    def addHerbivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresH.append(alimento)
        elif tipoAnimal == 2:
            self.acuaticoH.append(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoH.append(alimento)
        elif tipoAnimal == 4:
            self.voladorH.append(alimento)
     def verificarCarnivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            return alimento in self.terrestresC
        elif tipoAnimal == 2:
            return alimento in self.acuaticoC
        elif tipoAnimal == 3:
            return alimento in self.semiAcuaticoC
        elif tipoAnimal == 4:
            return alimento in self.voladorC

    def verificarHerbivoros(self, alimento, tipoAnimal):
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
            self.terrestresC.remove(alimento)
        elif tipoAnimal == 2:
            self.acuaticoC.remove(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoC.remove(alimento)
        elif tipoAnimal == 4:
            self.voladorC.remove(alimento)
    
    def deleteAlimentoH(self,alimento,tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresH.remove(alimento)
        elif tipoAnimal == 2:
            self.acuaticoH.remove(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoH.remove(alimento)
        elif tipoAnimal == 4:
            self.voladorH.remove(alimento)

    def verificarCarnivoros(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            return alimento in self.terrestresC
        elif tipoAnimal == 2:
            return alimento in self.acuaticoC
        elif tipoAnimal == 3:
            return alimento in self.semiAcuaticoC
        elif tipoAnimal == 4:
            return alimento in self.voladorC

    def verificarHerbivoros(self, alimento, tipoAnimal):
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
            self.terrestresC.remove(alimento)
        elif tipoAnimal == 2:
            self.acuaticoC.remove(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoC.remove(alimento)
        elif tipoAnimal == 4:
            self.voladorC.remove(alimento)

    def deleteAlimentoH(self, alimento, tipoAnimal):
        if tipoAnimal == 1:
            self.terrestresH.remove(alimento)
        elif tipoAnimal == 2:
            self.acuaticoH.remove(alimento)
        elif tipoAnimal == 3:
            self.semiAcuaticoH.remove(alimento)
        elif tipoAnimal == 4:
            self.voladorH.remove(alimento)